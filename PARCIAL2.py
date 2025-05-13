import heapq
import json
import os
from datetime import datetime

DATA_FILE = 'tareas.json'

class Tarea:
    def __init__(self, nombre, prioridad, fecha_vencimiento, dependencias):
        self.nombre = nombre
        self.prioridad = int(prioridad)
        self.fecha_vencimiento = fecha_vencimiento
        self.dependencias = dependencias or []

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'prioridad': self.prioridad,
            'fecha_vencimiento': self.fecha_vencimiento,
            'dependencias': self.dependencias
        }

    @staticmethod
    def from_dict(data):
        return Tarea(data['nombre'], data['prioridad'], data['fecha_vencimiento'], data['dependencias'])

class GestorTareas:
    def __init__(self):
        self.tareas = {}
        self.cargar_tareas()

    def guardar_tareas(self):
        with open(DATA_FILE, 'w') as f:
            json.dump([t.to_dict() for t in self.tareas.values()], f, indent=4)

    def cargar_tareas(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                tareas_data = json.load(f)
                for data in tareas_data:
                    tarea = Tarea.from_dict(data)
                    self.tareas[tarea.nombre] = tarea

    def añadir_tarea(self, nombre, prioridad, fecha_vencimiento, dependencias):
        if not nombre.strip():
            print("Error: El nombre de la tarea no puede estar vacío.")
            return
        if not isinstance(prioridad, int):
            print("Error: La prioridad debe ser un número entero.")
            return
        if nombre in self.tareas:
            print("Error: Ya existe una tarea con ese nombre.")
            return
        tarea = Tarea(nombre, prioridad, fecha_vencimiento, dependencias)
        self.tareas[nombre] = tarea
        self.guardar_tareas()
        print("Tarea añadida con éxito.")

    def mostrar_tareas(self, ordenar_por='prioridad'):
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        tareas_ordenadas = list(self.tareas.values())
        if ordenar_por == 'prioridad':
            tareas_ordenadas.sort(key=lambda x: x.prioridad)
        elif ordenar_por == 'fecha':
            tareas_ordenadas.sort(key=lambda x: datetime.strptime(x.fecha_vencimiento, '%Y-%m-%d'))

        for t in tareas_ordenadas:
            print(f" {t.nombre} | Prioridad: {t.prioridad} | Vence: {t.fecha_vencimiento} | Depende de: {t.dependencias}")

    def completar_tarea(self, nombre):
        if nombre not in self.tareas:
            print("Error: Tarea no encontrada.")
            return
        # Eliminar la tarea
        del self.tareas[nombre]
        # Eliminarla de las dependencias de otras tareas
        for t in self.tareas.values():
            if nombre in t.dependencias:
                t.dependencias.remove(nombre)
        self.guardar_tareas()
        print("Tarea completada y eliminada.")

    def obtener_siguiente_tarea(self):
        heap = []
        for tarea in self.tareas.values():
            if not tarea.dependencias:
                fecha_dt = datetime.strptime(tarea.fecha_vencimiento, '%Y-%m-%d')
                heapq.heappush(heap, (tarea.prioridad, fecha_dt, tarea))

        if not heap:
            print("No hay tareas disponibles sin dependencias.")
            return

        _, _, tarea = heapq.heappop(heap)
        print(f"Siguiente tarea: {tarea.nombre} | Prioridad: {tarea.prioridad} | Vence: {tarea.fecha_vencimiento}")


# === INTERFAZ DE PRUEBA BÁSICA ===

if __name__ == "__main__":
    gestor = GestorTareas()

    while True:
        print("\n--- MENÚ ---")
        print("1. Añadir tarea")
        print("2. Mostrar tareas (por prioridad)")
        print("3. Mostrar tareas (por fecha)")
        print("4. Completar tarea")
        print("5. Obtener siguiente tarea")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Nombre de la tarea: ")
            try:
                prioridad = int(input("Prioridad (número entero, menor = mayor prioridad): "))
            except ValueError:
                print(" Prioridad inválida.")
                continue
            fecha = input("Fecha de vencimiento (YYYY-MM-DD): ")
            dependencias = input("Dependencias (separadas por coma si hay): ").split(',')
            dependencias = [d.strip() for d in dependencias if d.strip()]
            gestor.añadir_tarea(nombre, prioridad, fecha, dependencias)

        elif opcion == '2':
            gestor.mostrar_tareas('prioridad')

        elif opcion == '3':
            gestor.mostrar_tareas('fecha')

        elif opcion == '4':
            nombre = input("Nombre de la tarea a completar: ")
            gestor.completar_tarea(nombre)

        elif opcion == '5':
            gestor.obtener_siguiente_tarea()

        elif opcion == '6':
            break

        else:
            print(" Opción inválida.")

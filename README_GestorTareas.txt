GESTOR DE TAREAS CON PRIORIDADES Y DEPENDENCIAS 

Este programa es un gestor de tareas que permite crear tareas con prioridades, fechas de vencimiento y dependencias entre ellas. Las tareas se almacenan en un archivo para que no se pierdan entre ejecuciones.

REQUISITOS

- Tener Python 3.7 o superior instalado.
- No se necesita instalar librerías externas. Todo usa librerías estándar de Python.

ARCHIVOS DEL PROYECTO

- gestor_tareas.py: El programa principal.
- tareas.json: Archivo que guarda tus tareas (se crea automáticamente).
- README.md: Instrucciones de uso (este contenido).

CÓMO EJECUTAR EL PROGRAMA

1. Abre una terminal.

2. Ve al directorio donde está guardado el archivo. 

3. Ejecuta el script con Python:

FUNCIONALIDADES DISPONIBLES

Al ejecutar el programa, aparece un menú como este:

--- MENÚ ---
1. Añadir tarea
2. Mostrar tareas (por prioridad)
3. Mostrar tareas (por fecha)
4. Completar tarea
5. Obtener siguiente tarea
6. Salir

1. Añadir tarea
Introduce:
- Nombre de la tarea (ejemplo: Estudiar)
- Prioridad (un número entero, donde 1 es la prioridad más alta)
- Fecha de vencimiento (YYYY-MM-DD)
- Dependencias (otras tareas que deben completarse antes, separadas por comas, o déjalo vacío si no hay)

2. Mostrar tareas (por prioridad)
Lista todas las tareas ordenadas desde la prioridad más alta a la más baja.

3. Mostrar tareas (por fecha)
Lista todas las tareas ordenadas por la fecha de vencimiento más cercana.

4. Completar tarea
Marca una tarea como completada, la elimina del sistema y de las dependencias de otras tareas.

5. Obtener siguiente tarea
Muestra la próxima tarea disponible (sin dependencias pendientes) con mayor prioridad.

6. Salir
Cierra el programa. Las tareas se guardan automáticamente en el archivo tareas.json.

PERSISTENCIA DE DATOS

Todas las tareas se guardan automáticamente en un archivo llamado tareas.json, así que no se pierden aunque cierres el programa.


INFROMACION ADICIONAL

- Si una tarea tiene dependencias, no puede ejecutarse hasta que todas esas dependencias estén completadas.
- El programa valida que:
  - El nombre de la tarea no esté vacío.
  - La prioridad sea un número entero.
  - No se repita el nombre de una tarea.
- Si introduces una fecha incorrecta o un formato inválido, el programa lo detecta y muestra un mensaje de error.

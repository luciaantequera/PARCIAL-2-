📋 GESTOR DE TAREAS CON PRIORIDADES Y DEPENDENCIAS (PYTHON)

Este programa es un gestor de tareas que permite crear tareas con prioridades, fechas de vencimiento y dependencias entre ellas. Las tareas se almacenan en un archivo para que no se pierdan entre ejecuciones.

🚀 REQUISITOS

- Tener Python 3.7 o superior instalado.
- No necesitas instalar librerías externas. Todo usa librerías estándar de Python.

📁 ARCHIVOS DEL PROYECTO

- gestor_tareas.py: El programa principal.
- tareas.json: Archivo que guarda tus tareas (se crea automáticamente).
- README.md: Instrucciones de uso (este contenido).

▶️ CÓMO EJECUTAR EL PROGRAMA

1. Abre una terminal o línea de comandos.

2. Ve al directorio donde está guardado el archivo. Por ejemplo:

   En Windows:
   cd C:\ruta\del\proyecto

   En macOS/Linux:
   cd /home/usuario/ruta/del/proyecto

3. Ejecuta el script con Python:

   En Windows:
   python gestor_tareas.py

   En macOS/Linux (a veces necesitas usar python3):
   python3 gestor_tareas.py

📌 FUNCIONALIDADES DISPONIBLES

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

💾 PERSISTENCIA DE DATOS

Todas las tareas se guardan automáticamente en un archivo llamado tareas.json, así que no se pierden aunque cierres el programa.

🧪 EJEMPLO DE USO RÁPIDO

1. Añadir la tarea T1 (prioridad 1, vence en 2025-05-20, sin dependencias)
2. Añadir la tarea T2 (prioridad 2, vence en 2025-05-19, depende de T1)
3. Obtener siguiente tarea → se mostrará T1
4. Completar T1
5. Obtener siguiente tarea → ahora se mostrará T2

ℹ️ NOTAS

- Si una tarea tiene dependencias, no puede ejecutarse hasta que todas esas dependencias estén completadas.
- El programa valida que:
  - El nombre de la tarea no esté vacío.
  - La prioridad sea un número entero.
  - No se repita el nombre de una tarea.
- Si introduces una fecha incorrecta o un formato inválido, el programa lo detecta y muestra un mensaje de error.

📞 SOPORTE

Si necesitas ayuda para ejecutar este script:
- Pide ayuda a alguien con conocimientos básicos de Python.
- Consulta foros como Stack Overflow.

¡Disfruta organizando tus tareas y siendo más productivo! ✅
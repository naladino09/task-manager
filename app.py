def agregar_tarea():
    tarea = input("Escribe la tarea: ")
    with open("tareas.txt", "a") as f:
        f.write(tarea + "\n")
    print("Tarea agregada")

def ver_tareas():
    print("\n--- TAREAS ---")
    try:
        with open("tareas.txt", "r") as f:
            print(f.read())
    except:
        print("No hay tareas")

def limpiar_tareas():
    open("tareas.txt", "w").close()
    print("Tareas eliminadas")

while True:
    print("\n1. Agregar")
    print("2. Ver")
    print("3. Limpiar")
    print("4. Salir")

    opcion = input("> ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        limpiar_tareas()
    elif opcion == "4":
        break
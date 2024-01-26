from Tarea import Tarea
from Listatarea import Listatarea


def main():
    lista_tarea = Listatarea()

    while True:
        print("\n----- Menú Principal -----")
        print("1. Agregar Tarea")
        print("2. Mostrar Tareas")
        print("3. Eliminar Tarea")
        print("4. Modificar Tarea")
        print("5. Filtrar Tareas por Prioridad")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
            prioridad = input("Ingrese la prioridad de la tarea: ")
            
            tarea_nueva = Tarea(titulo, descripcion, fecha_vencimiento, prioridad)
            lista_tarea.agregar_tarea(tarea_nueva)
            print("Tarea agregada exitosamente.")

        elif opcion == "2":
            print("\n----- Lista de Tareas -----")
            lista_tarea.mostrar_tareas()

        elif opcion == "3":
            titulo_eliminar = input("Ingrese el título de la tarea a eliminar: ")
            lista_tarea.eliminar_tarea(titulo_eliminar)

        elif opcion == "4":
            titulo_modificar = input("Ingrese el título de la tarea a modificar: ")
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
            nueva_fecha = input("Ingrese la nueva fecha de vencimiento (YYYY-MM-DD): ")
            nueva_prioridad = input("Ingrese la nueva prioridad de la tarea: ")
            
            lista_tarea.modificar_tarea(titulo_modificar, nueva_descripcion, nueva_fecha, nueva_prioridad)

        elif opcion == "5":
            prioridad_filtrar = input("Ingrese la prioridad para filtrar las tareas: ")
            lista_tarea.filtrar_por_prioridad(prioridad_filtrar)

        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()

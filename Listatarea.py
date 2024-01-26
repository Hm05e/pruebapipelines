class Listatarea:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for tarea in self.tareas:
                print(tarea)

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"Tarea '{titulo}' eliminada.")
                return
        print(f"No se encontró la tarea '{titulo}'.")

    def modificar_tarea(self, titulo, nueva_descripcion, nueva_fecha, nueva_prioridad):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.descripcion = nueva_descripcion
                tarea.fecha_vencimiento = nueva_fecha
                tarea.prioridad = nueva_prioridad
                print(f"Tarea '{titulo}' modificada.")
                return
        print(f"No se encontró la tarea '{titulo}'.")

    def filtrar_por_prioridad(self, prioridad):
        tareas_filtradas = [tarea for tarea in self.tareas if tarea.prioridad == prioridad]
        if not tareas_filtradas:
            print(f"No hay tareas con prioridad '{prioridad}'.")
        else:
            print(f"Tareas con prioridad '{prioridad}':")
            for tarea in tareas_filtradas:
                print(tarea)

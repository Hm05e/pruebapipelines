class Tarea:
    def __init__(self, titulo, descripcion, fecha_vencimiento, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.titulo} - {self.descripcion} - {self.fecha_vencimiento} - {self.prioridad}"

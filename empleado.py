from datetime import datetime

class Empleado:
    def __init__(self, id, nombre, departamento, fecha_contratacion):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento
        self.fecha_contratacion = fecha_contratacion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Departamento: {self.departamento}, Fecha de Contratación: {self.fecha_contratacion.strftime('%d/%m/%Y')}"

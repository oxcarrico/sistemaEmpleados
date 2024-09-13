from empleado import Empleado
from datetime import datetime

class SistemaEmpleados:
    def __init__(self):
        self.empleados = {}
        
    def agregar_empleado(self, id, nombre, departamento, fecha_contratacion):
        if id in self.empleados:
            print("Empleado con ese id ya existe")
        else: 
            self.empleados[id] = Empleado(id, nombre, departamento, fecha_contratacion)
            print("empleado añadido con existo :)")
    
    def buscar_empleado(self, id):
        empleado = self.empleados.get(id)
        if empleado:
            print(empleado)
        else:
            print("Un empleado con ese id no esta registrado")
            
    def actualizar_empleado(self, id, nombre=None, departamento=None, fecha_contratacion=None):
        empleado = self.empleados.get(id)
        if empleado:
            if nombre:
                empleado.nombre = nombre
            if departamento:
                empleado.departamento = departamento
            if fecha_contratacion:
                empleado.fecha_contratacion = fecha_contratacion
            print("Empleado actualizado exitosamente.")
        else:
            print("Empleado no encontrado.")
    
    def eliminar_empleados(self, id):
        if id in self.empleados:
            del self.empleados[id]
            print("Emplado eliminado exitosamente.")
        else:
            print("Empleado no encontrado.")
from sistema_empleados import SistemaEmpleados
from datetime import datetime 

def menu():
    sistema = SistemaEmpleados()
    
    while True:
        print("____Menu____")
        print("1. Agregar empleado")
        print("2. Buscar empleado")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Salir")
        opcion = int(input("¿Que quieres hacer?: "))
        
        if opcion == 1:
            id = (input("Elige el id: "))
            nombre = (input("Elige el nombre: "))
            departamento = (input("Elige el departamento:"))
            fecha = input("Ingresa la fecha de contratación (dd/mm/yyyy): ")     
            fecha_contratacion = datetime.strptime(fecha, "%d/%m/%Y")   
            sistema.agregar_empleado(id, nombre, departamento, fecha_contratacion )
        elif opcion == 2:
            id = input("Ingresa el id del empleado a buscar: ")
            sistema.buscar_empleado(id)
        elif opcion == 3:
            id = input("Ingresa el id")
            nombre = input("Ingresa el nombre")
            departamento = input("ingresa el apartamento")
            fecha = input("Ingresa la fecha")
            fecha_contratacion = datetime.strptime(fecha, "%d/%m/%Y") if fecha else None
            sistema.actualizar_empleado(id, nombre, departamento, fecha_contratacion)
        elif opcion == 4:
            id = input("Escribe el id del empleado a borrar: ")
            sistema.eliminar_empleados(id)
        elif opcion == 5:
            print("Saliendo...") 
            break
        else:
            print("Opcion no valida")
menu()
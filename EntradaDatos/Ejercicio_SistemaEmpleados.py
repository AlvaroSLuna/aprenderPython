# Crea un programa para solicitar información de un empleado, introduciendo datos por consola
# Nombre, edad (int), Salario (float) y si es jefe de departamento (bool)

print("*** Sistema de Empresa ***")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
salario = float(input("Introduce tu salario: "))
es_jefe = input("Eres jefe de departamento (Si/No): ")

# Vamos a convertir a un tipo bool la variable es_jefe
es_jefe = es_jefe.lower() == 'si'

# Imprimir los valores del empleado
print('\nDatos del Empleado')
print(f"El nombre del empleado es {nombre}")
print(f"La edad del empleado es {edad}")
print(f"El salario del empleado es {salario: .2f}")
print(f"Es jefe de departamento? {es_jefe}")
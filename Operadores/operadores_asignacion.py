print('*** Operadores de asignacion ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde python'
print(f'Valor de cadena: {cadena}')

# Asignación multiple
numero_a, numero_b, numero_c = 1, 2, 3
print(f'Valor de numero a: {numero_a}')
print(f'Valor de numero b: {numero_b}')
print(f'Valor de numero c: {numero_c}')

variable_a, variable_b, variable_c = 10, 'Saludos', 10.6
print(f'Valor de variable_a: {variable_a}')
print(f'Valor de variable_b: {variable_b}')
print(f'Valor de variable_c: {variable_c}')

#Asignacion encadenada

a = b = c = 10
print(f'Valor de a: {a}, b: {b}, c: {c}') # Valor de a: 10, b: 10, c: 10

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales de x: {x}, y: {y}')
# Aplicando el concepto de asignación multiple, intercambiamos valores
x, y = y, x
print(f'Invertir los valores de x: {x}, y: {y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido con una coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')
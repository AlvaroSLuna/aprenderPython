print(f'*** Sentencia if ***')

edad = int(input('Introduzca su edad: '))
if edad >= 18:
    print(f'Eres mayor de edad, tienes {edad} años')
elif 13 <= edad < 18:
    print(f'Eres un adolescente, tienes {edad} años')
else:
    print(f'Eres un niño, tienes {edad} años')
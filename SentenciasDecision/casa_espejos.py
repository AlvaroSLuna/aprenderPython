print('*** Bienvenidos a la Casa de los Espejos ***')

miedo_oscuridad_txt = input('Tienes miedo a la oscuridad (Si/No)? ')
edad = int(input('Pon tu edad: '))
miedo_oscuridad = miedo_oscuridad_txt.strip().lower() == 'si'
MAYOR_EDAD = 10

if not miedo_oscuridad and edad >= MAYOR_EDAD:
    print('Cumples las condiciones para entrar a la casa de los espejos')

else:
    print('No cumples las condiciones para entrar a la casa de los espejos')
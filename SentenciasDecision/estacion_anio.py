print('*** Estaciones del año ***')

mes = int(input('Ingresa el mes del año de forma numérica: '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Estación Desconocida'

# Imprimimos el resultado
print(f'La estación del mes {mes} es {estacion}')
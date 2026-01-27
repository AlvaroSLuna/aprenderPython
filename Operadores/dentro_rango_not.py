# Vamos a revisar si una variable se encuentra dentro de rango entre 1 y 10
dato = int(input('Proporciona un dato entero: '))

# Revisamos si esta dentro de rango

# esta_dentro_rango = 1 <= dato <= 10
# print(f'Variable está dentro de rango (entre 1 y 10)?: {esta_dentro_rango}')

# Revisamos la lógia inversa, si el dato está fuera de rango
esta_fuera_rango = not(1 <= dato <= 10)
print(f'Variable está fuera de rango (entre 1 y 10): {esta_fuera_rango}')
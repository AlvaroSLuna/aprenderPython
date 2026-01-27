print("*** Sistema de Autenticación ***")

VALOR_MINIMO = 0
VALOR_MAXIMO = 5

#Solicitamos un valor entre 0 y 5
valor_usuario = int(input(f'Ingresa un valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

# Verificamos si el dato se encuentra dentro de rango
# dentro_rango = valor_usuario >= VALOR_MINIMO and valor_usuario <= VALOR_MAXIMO
dentro_rango = VALOR_MINIMO <= valor_usuario <= VALOR_MAXIMO

print(f"Valor esta dentro de rango?: {dentro_rango}")
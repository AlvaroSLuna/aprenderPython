print('*** Bienvenidos a la Aplicación de Salud y Fitness ***')

# Pedimos valores al usuario
nombre_usuario = input('Nombre del usuario: ')
pasos_caminados = int(input('Pasos caminados hoy: '))

# Constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASOS = 0.04 # Valor aprox. en kilocalorias

# Calculamos calorias quemadas
calorias_quemadas = pasos_caminados * CALORIAS_POR_PASOS

# Verificamos si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_caminados >= META_PASOS_DIARIOS
meta_alcanzada_txt = 'Sí' if meta_alcanzada else 'No'

# Mostramos información

print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos caminados hoy: {pasos_caminados}')
print(f'Calorías quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos dirarios alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIOS} pasos')
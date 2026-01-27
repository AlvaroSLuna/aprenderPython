print('*** Bienvenidos al Sistema de Reserva del Hotel ***')

nombre_cliente = input('Nombre del cliente: ')
dias_estancia = int(input('Dias de estancia en el hotel: '))
tiene_vistas_txt = input('Cuarto con vistas al mar (Si/No): ')
tiene_vistas = tiene_vistas_txt.strip().lower() == 'si'

PRECIO_CUARTO = 150.50
PRECIO_CUARTO_VISTAS = 190.50

precio_habitacion_vistas = PRECIO_CUARTO_VISTAS * dias_estancia
precio_habitacion_sin_vistas = PRECIO_CUARTO * dias_estancia


print('-------------- Detalles de la Reservación --------------')
if tiene_vistas:
    print(f'Cliente: {nombre_cliente}')
    print(f'Dias de estancia: {dias_estancia}')
    print(f'Costo total: {precio_habitacion_vistas}€')
    print(f'Habitación con vistas al mar: {tiene_vistas_txt}')

else:
    print(f'Cliente: {nombre_cliente}')
    print(f'Dias de estancia: {dias_estancia}')
    print(f'Costo total: {precio_habitacion_sin_vistas}€')
    print(f'Habitación con vistas al mar: {tiene_vistas_txt}')
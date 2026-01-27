print('*** Sistema Tienda en Línea con Descuentos ***')

dinero_gastado = float(input("Cuanto dinero se ha dejado en la tienda en €: "))
es_miembro = input('Eres miembro de la tienda (Si/No)? ')

if es_miembro.strip().lower() == 'si' and dinero_gastado >= 1000:
    print('Felicidades, has obtenido un descuento del 10%')
    print(f'Costo de la compra: {dinero_gastado:.2f}€')
    descuento = dinero_gastado * 0.1
    print(f'Descuento de: {descuento:.2f}€')
    costo_final = dinero_gastado - descuento
    print(f'Costo dinal de la compra con descuento: {costo_final:.2f}€')

elif es_miembro.strip().lower() == 'si':
    print('Felicidades, has obtenido un descuento del 5%')
    print(f'Costo de la compra: {dinero_gastado:.2f}€')
    descuento = dinero_gastado * 0.05
    print(f'Descuento de: {descuento:.2f}€')
    costo_final = dinero_gastado - descuento
    print(f'Costo dinal de la compra con descuento: {costo_final:.2f}€')

else:
    print('No obtuviste ningún descuento')
    print('Te invitamos a se miembro de la tienda')
    print(f'Costo de la compra: {dinero_gastado:.2f}€')
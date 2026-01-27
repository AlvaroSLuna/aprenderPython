print("*** Generación Ticket Venta ***")

precio_leche = float(input("\nPrecio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio plátanos: "))
descuento_porcentaje = int(input("Aplicar algun descuento (%)? "))

# Cálculo subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Calculamos porcentaje
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_descuento = subtotal - descuento

# Cálculo con impuestos (21%)
impuesto = subtotal_descuento * 0.21

# Calculo total de la compra con impuestos
costo_total = subtotal_descuento + impuesto
print(f"""
Subtotal: {subtotal:.2f}€
Descuento: {descuento:.2f} ({descuento_porcentaje}%)
Subtotal con descuento: {subtotal_descuento:.2f}€
Impuesto (21%): {impuesto:.2f}€
Costo total de la compra: {costo_total:.2f}€
""")
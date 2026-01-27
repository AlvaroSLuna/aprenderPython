print("*** Operador or ***")

condicion1 = False
condicion2 = False
condicion3 = True
# El operador or regresa True si cualquiera de los operandos es True
resultado = condicion1 or condicion2
resultado1 = condicion3 or condicion2
print(f"Resultado {condicion1} or {condicion2} es: {resultado}") # Regresa False
print(f"Resultado {condicion3} or {condicion2} es: {resultado1}") # Regresa True
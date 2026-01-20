# Programa: Función bool

# 1. Números (int y float)
print("Al poner un 0 el resultado es:", bool(0))        # False
print("Al poner un 0.0 el resultado es:",bool(0.0))     # False
print("Al poner un 42 el resultado es:",bool(42))       # True

# 2. Texto (Cadena)
# Cadena vacía = Nada = False
print("Al no poner nada en la cadena da:",bool(""))     # False

# Cadena con espacio o texto = Algo = True
print("Al tener un espacio dentro de la cadena da:", bool(" "))     # True
print("Al tener Hola dentro de la cadena da:", bool("Hola"))        # True

# 3. None (Ausencia de valor)
vacio = None
print('Al no tener valor da:',bool(vacio))      # False

print(bool(False))      # False
print(bool(True))       # False
# Programa: Aplicar el concepto de slicing

texto = "PROGRAMACION"

# 1. Básico [inicio:fin]
print(texto[0:4]) # "PROG" (El indice 4 no se incluye)

# 2. Atajo desde el inicio [:fin]
print(texto[:4]) # "PROG" (Asume inicio 0)

# 3. Atajo hasta el final [inicio:]
print(texto[8:]) # "CION" (Hasta el ultimo char)

# 4. Índices negativos
print(texto[-4:]) # "CION" ( Los ultimos 4)
print(texto[-12:-8]) # "PROG"

# 5. Pasos [::paso] (Invertir cadena)
print(texto[::-1]) # "NOICAMARGORP"

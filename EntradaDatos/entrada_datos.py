# Programa: Entrada de Datos Python
nombre = input("Introduce tu nombre: ")
print(f"Tu nombre es {nombre}")

# Cuidado con la conversión de datos al trabajar con valores numéricos
# Forma Correcta: Envolver con int () o float ()

# Para enteros (edad, cantidad)
edad = int(input("Introduce tu edad: "))
print(f"Tu edad es {edad}")
print(edad + 5) # 20 + 5 = 25

# Para decimales (precio, altura)
altura = float(input("Introduce tu altura: "))
print(f"Tu altura es {altura}")
print(altura - 0.5)
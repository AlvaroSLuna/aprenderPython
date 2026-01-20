# Programa: Convertir tipos en Python

# Definimos una variable de tipo String
numero_texto = "50"

total = int(numero_texto) + 10
print(f"El total es: {total}")

concatenacion = numero_texto + str(10)
print(f"Resultado de la concatenacion: {concatenacion}")

# Si el número es decimal usamos float()

numerodecimal_texto = '10.23'
sumadeciamles = float(numerodecimal_texto) + 23.27
print(f"Resultado de la suma: {sumadeciamles}")

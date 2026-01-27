print("*** Revisión Valor Positivo ***")

numero = int(input("Introduce un numero: "))

if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero < 0:
    print(f"El numero {numero} es negativo")
else:
    print(f"El numero {numero} es cero")
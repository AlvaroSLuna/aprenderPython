print('*** Comparador de números ***')

numero1 = int(input('Introduce el primer número: '))
numero2 = int(input('Introduce el segundo número: '))

if numero1 > numero2:
    print(f'El {numero1} es mayor que {numero2}')
elif numero1 < numero2:
    print(f'El {numero2} es mayor que {numero1}')
elif numero1 == numero2:
    print(f'El {numero1} y {numero2} son iguales')
else:
    print('Introduce valores válidos')
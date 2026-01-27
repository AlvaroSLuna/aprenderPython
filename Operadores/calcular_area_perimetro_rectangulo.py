print("*** Calculo Área y Perímetro Rectangulo ***")

base = float(input("Cual es la base de tu rectángulo?: "))
altura = float(input("Cual es la altura del rectángulo?: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f'El area de tu rectangulo es de: {area} y el perimetro es de: {perimetro}')
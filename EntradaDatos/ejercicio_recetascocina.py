# Programa para solicitar algunos valores importantes para una receta de cocina.
# Los valores son: Nombre de la receta, ingredientes, tiempo de preparación en minutos y dificultad (Fácil, Media, Alta)

print("*** Receta de Cocina ***")

# Variables necesarias para la receta
nombre_receta = input("Introduce el nombre: ")
ingredientes_receta = input("Introduce los ingredientes: ")
tiempo_preparacion = int(input("Introduce el tiempo preparación (min): "))
dificultad_receta = input("Introduce la dificultad: ")

print("---------------------")

# Imprimimos por pantalla la información
print(f"Nombre receta: {nombre_receta}")
print(f"Ingredientes: {ingredientes_receta}")
print(f"Tiempo preparación: {tiempo_preparacion}")
print(f"Dificultad: {dificultad_receta}")
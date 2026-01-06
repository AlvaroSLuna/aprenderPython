# Ejemplo: Cadenas inmutables

animal = "Gato"

# animal[4] = "s" # Provoca un error
# CORRECTO: Concatenar (Sumar)
# Tomamos "Gato" + "s" y lo guardamos en una nueva variable
plural = animal + "s"

print(animal) # Salida: Gato (Intacto)
print(plural) # Salida: Gatos (Nuevo Objeto)

plural = f"{animal}s"
print(plural) # Salida: Gatos (Nuevo Objeto)
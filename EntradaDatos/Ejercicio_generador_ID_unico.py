# Con los datos recibidos el sistema deberá realizar lo siguiente:
# Del valor recibido de nombre, usar solo 2 primeras letras y convertirlas a mayúsculas
# Del valor apellido usar las 2 primeras letras y convertirlas a mayúsculas
# Del valor de año, tomar los 2 ultimos digitos

# Además, con ranint se deberan generar 4 dígitos aleatorios
# Finalmente con todos los datos obtenidos generamos un ID único
from random import randint
print("*** Sistema generador de ID Único ***")

# Pedimos al usuario la información necesaria con las variables
nombre = input("Introduce el nombre: ")
apellido = input("Introduce el apellido: ")
anio_nacimiento = input("Introduce el año de nacimiento (YYYY): ")

# Procedemos a seleccionar las dos primeras letras del nombre y apellido, las ponemos en mayúsculas
# y los dos últimos dígitos del año

nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:]

# Generamos el valor aleatorio
numero_aleatorio = randint(1000, 9999)

# Generamos el valor de id único
id_unico = f"{nombre_2}{apellido_2}{anio_nacimiento_2}{numero_aleatorio}"

print(f"""\nHola {nombre},
    Tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    Felicidades!!!
""")
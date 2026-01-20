# Para generar un email se debe solicitar: Nombre, apellidos, nombre empresa y extensión dominio

print('*** Generador de Emails ***')

# Pedimos los datos al usuario:

nombre = input('Introduzca  su nombre: ')
apellido = input('Introduzca  su apellido: ')
nombre_empresa = input('Introduzca nombre de la empresa: ')
extension_dominio = input('Introduzca extension de dominio de tu empresa: ')

# Ahora procesamos los datos

nombre_normalizado = nombre.strip().lower().replace(' ', '.')
apellido_normalizado = apellido.strip().lower().replace(' ', '.')
nombre_empresa_normalizado = nombre_empresa.strip().lower().replace(' ', '')
extension_dominio = extension_dominio.strip().lower().replace(' ', '')

email = f"{nombre_normalizado}.{apellido_normalizado}@{nombre_empresa_normalizado}{extension_dominio}"
print("--------------------------------")
print(f""" 
Hola {nombre},
    Su email ha sido generado:
    {email}
    Enhorabuena!!!
""")
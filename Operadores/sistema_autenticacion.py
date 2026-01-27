print("*** Sistema de Autenticación ***")
USUARIO_REAL = 'Ronson19'
PASSWORD_REAL = 'Joselito1289'

usuario = input("Ingrese su usuario: ")
password = input('Ingrese su contraseña: ')

datos_correctos = (USUARIO_REAL == usuario.strip()
                   and PASSWORD_REAL == password.strip())
print(f"Datos correctos? {datos_correctos}")
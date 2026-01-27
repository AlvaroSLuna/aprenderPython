print('*** Bienvenidos al Sistema Bancario ***')

salir_sistema_txt = input('Salir sistema? [Si/No]?: ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si' # Si el usuario dice Si, regresa True, si dice No regresa False

# Si no deseamos salir del sistema
if not salir_sistema:
    print('Continuamos dentro del sistema')
# Si deseamos salir
else:
    print('Saliendo del sistema')
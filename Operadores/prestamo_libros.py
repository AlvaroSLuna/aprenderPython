print("*** Sistema Préstamo Libros ***")

DISTANCIA_MAXIMA_BIBLIOTECA = 3
distancia_estudiante = int(input('Dime a cuantos kilometros estas de la biblioteca: '))
tiene_credencial = input("Tienes la credencial de estudiante? (Si/No)?: ")

puede_prestamo = (distancia_estudiante <= DISTANCIA_MAXIMA_BIBLIOTECA
                  or tiene_credencial.strip().lower() == 'si')

print(f"Se le presta el libro? {puede_prestamo}")
# ERROR COMÚN DE PRINCIPIANTE
respuesta_usuario = "False" # Es un texto

# La función bool evalúa si el string está vacío
es_verdad = bool(respuesta_usuario)

print(f"El valor es: {es_verdad}")
# Output: El valor es: True
# Por que? Porque el string "False" tiene 5 letras. NO está vacío.

# Forma correcta de validar vacío:
texto_vacio = ""
print(bool(texto_vacio))        # False
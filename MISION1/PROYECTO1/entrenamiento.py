# librerías 
import re
"""
Expresiones regulares en python
Problemas reales
"""
# Código
print("Librería cargada correctamente")
# Ejemplo1
texto="Mi número es 1234"
resultado=re.search(r"\d+",texto)
print(resultado.group())
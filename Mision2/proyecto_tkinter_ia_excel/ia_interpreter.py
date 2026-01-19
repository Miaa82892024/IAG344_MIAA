# ia_interpreter.py
# Simula una IA básica para validar instrucciones en lenguaje natural

import re


def interpretar_texto(texto):
    """
    Interpreta y valida una instrucción en lenguaje natural.
    Retorna un resumen de la intención del usuario.
    """
    if not texto or not texto.strip():
        raise ValueError("La instrucción está vacía")

    texto = texto.lower()

    # Intención: limpiar identificadores
    if re.search(r"\blimpia(r)?\b", texto):
        return "Limpieza de identificadores detectada"

    # Intención: unir nombre y apellido
    if re.search(r"\bune\b|\bunir\b", texto) and "nombre" in texto:
        return "Unión de nombre y apellido detectada"

    # Intención general de procesamiento
    if "procesa" in texto or "excel" in texto:
        return "Procesamiento de archivo Excel detectado"

    raise ValueError("No se pudo interpretar la instrucción")

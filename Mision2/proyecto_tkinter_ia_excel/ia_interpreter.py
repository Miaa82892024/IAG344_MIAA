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
    
    instruccion={
        "accion":None,
        "extra_colum":None
    }
    
    #Detectar columna (ej: columna B, columna F)
    match_col=instruccion["extra_column"]=match.col.group(1).upper()

    # Intención: limpiar identificadores
    if re.search(r"\blimpia(r)?\b", texto):
        instruccion["accion"]="limpiar"
        
    # Intención: unir nombre y apellido
    if re.search(r"\bune\b|\bunir\b", texto) and "nombre" in texto:
        instruccion["accion"]="unir"
        
    if not instruccion["accion"]:
        raise ValueError("No se pudo interpretar la insrrucción")
    
    return instruccion
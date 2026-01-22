# controller.py
# Coordina la interfaz, la IA y la lógica de interpretación

from ia_interpreter import interpretar_texto
from processor import ejecutar_accion



def procesar_instruccion(texto, path):
    """
    Procesa una instrucción en lenguaje natural.
    Por ahora solo valida e interpreta el texto.
    """
    try:
        instruccion = interpretar_texto(texto)
        
        if not instruccion:
            return False, "No se pudo interpretar la instrucción"
        
        ejecutar_accion(path, instruccion)

        # En esta versión solo se valida la instrucción
        return True, f"Instrucción interpretada correctamente: {instruccion}"

    except Exception as e:
        return False, f"Error al procesar la instrucción: {str(e)}"

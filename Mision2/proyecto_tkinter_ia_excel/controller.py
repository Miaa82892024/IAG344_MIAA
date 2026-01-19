# controller.py
# Coordina la interfaz, la IA y la lógica de interpretación

from ia_interpreter import interpretar_texto


def procesar_instruccion(texto):
    """
    Procesa una instrucción en lenguaje natural.
    Por ahora solo valida e interpreta el texto.
    """
    try:
        instruccion = interpretar_texto(texto)

        if not instruccion:
            return False, "No se pudo interpretar la instrucción"

        # En esta versión solo se valida la instrucción
        return True, f"Instrucción interpretada correctamente: {instruccion}"

    except Exception as e:
        return False, f"Error al procesar la instrucción: {str(e)}"

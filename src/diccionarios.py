# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    Las palabras se comparan en minúsculas para pasar los tests case-insensitive.
    """
    palabras = texto.lower().split()
    frecuencia = {}
    for p in palabras:
        frecuencia[p] = frecuencia.get(p, 0) + 1
    return frecuencia


def invertir_diccionario(d: dict) -> dict:
    """
    Retorna un nuevo diccionario con claves y valores intercambiados.
    """
    return {valor: clave for clave, valor in d.items()}


def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios. 
    Si hay claves repetidas, el desempaquetado de d2 al final asegura que prevalezca.
    """
    return {**d1, **d2}


def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Retorna un nuevo diccionario con solo los pares
    cuyo valor sea >= minimo.
    """
    return {k: v for k, v in d.items() if v >= minimo}
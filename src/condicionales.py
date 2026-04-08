# ============================================================
# MÓDULO 2: Condicionales
# ============================================================


def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo" (incluye el 0 según preferencia) o "negativo".
    """
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"


def mayor_de_tres(a: int, b: int, c: int) -> int:
    """
    Retorna el mayor de tres números usando la función built-in max.
    """
    return max(a, b, c)


def clasificar_nota(nota: float) -> str:
    """
    Retorna la categoría de la nota con validación de rango.
    """
    if nota < 0 or nota > 10:
        return "Nota inválida"
    
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"


def es_bisiesto(anio: int) -> bool:
    """
    Retorna True si el año es bisiesto usando lógica compacta.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
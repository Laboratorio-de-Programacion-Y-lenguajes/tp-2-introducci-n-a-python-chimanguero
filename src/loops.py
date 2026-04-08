# ============================================================
# MÓDULO 5: Loops
# ============================================================

def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    return list(range(1, n + 1))


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    """
    return [n * i for i in range(1, 11)]


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    """
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    Acorde a los tests: 1 no es primo, 2 sí lo es.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    serie = [0, 1]
    while len(serie) < n:
        proximo = serie[-1] + serie[-2]
        serie.append(proximo)
    
    return serie
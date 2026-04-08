# ============================================================
# MÓDULO 6: Funciones
# ============================================================


def aplicar_funcion(lista: list, func) -> list:
    """
    Aplica func a cada elemento de la lista y retorna la nueva lista.
    """
    return [func(x) for x in lista]


def componer(f, g):
    """
    Retorna una nueva función que aplica g y luego f.
    Ejemplo: componer(f, g)(x) == f(g(x))
    """
    def funcion_compuesta(x):
        return f(g(x))
    
    return funcion_compuesta


def memoizar(func):
    """
    Retorna una versión de func que cachea sus resultados.
    Usa un diccionario para evitar cálculos repetidos.
    """
    cache = {}

    def wrapper(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    
    return wrapper


def reducir(lista: list, func, inicial):
    """
    Aplica func acumulativamente a los elementos de lista,
    comenzando con inicial. NO usa functools.reduce.
    """
    acumulador = inicial
    for elemento in lista:
        acumulador = func(acumulador, elemento)
    return acumulador

# Ejemplo de uso rápido para verificar
if __name__ == "__main__":
    # Test rápido de reducción
    suma = reducir([1, 2, 3, 4], lambda a, b: a + b, 0)
    print(f"Suma total: {suma}") # Debería dar 10
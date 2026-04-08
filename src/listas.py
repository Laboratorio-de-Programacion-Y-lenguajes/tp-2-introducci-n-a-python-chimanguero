# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    Si la lista está vacía, sum() devuelve 0 por defecto.
    """
    return sum(numeros)


def filtrar_pares(numeros: list) -> list:
    """
    Retorna una nueva lista con solo los números pares usando list comprehension.
    """
    return [n for n in numeros if n % 2 == 0]


def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    El slicing [::-1] crea una copia nueva invertida.
    """
    return lista[::-1]


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin duplicados, manteniendo el orden.
    Usar dict.fromkeys es más eficiente que un set si el orden importa.
    """
    return list(dict.fromkeys(lista))


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    return [item for sublist in lista for item in sublist]
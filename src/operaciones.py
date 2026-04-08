# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    """
    # Limpiamos el texto: minúsculas y sin espacios
    texto_limpio = texto.lower().replace(" ", "")
    # Comparamos con su versión invertida
    return texto_limpio == texto_limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    """
    return texto.title()


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto.
    """
    vocales = "aeiou"
    return sum(1 for caracter in texto.lower() if caracter in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    """
    resultado = ""
    
    for caracter in texto:
        if caracter.isalpha():
            # Definimos si la base es 'A' (65) o 'a' (97)
            base = ord('A') if caracter.isupper() else ord('a')
            
            # Calculamos la nueva posición dentro del alfabeto (0-25)
            # El operador % 26 asegura que 'z' + 1 vuelva a 'a'
            nueva_posicion = (ord(caracter) - base + desplazamiento) % 26
            
            # Convertimos de nuevo a carácter
            resultado += chr(base + nueva_posicion)
        else:
            # Si no es letra (espacio, coma, etc.), queda igual
            resultado += caracter
            
    return resultado
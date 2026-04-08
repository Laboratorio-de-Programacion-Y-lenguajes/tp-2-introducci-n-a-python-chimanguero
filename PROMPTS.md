# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: Gemini 3 Flash

**Prompt usado**:
> Actuá como tutor de Python 3.13. Dame una receta paso a paso para completar el script `src/variables.py` de modo que pase los tests de `pytest`. 
> Los pasos deben incluir:
> 1) `crear_saludo(nombre)`: Retornar exactamente "Hola, {nombre}!" usando f-strings.
> 2) `suma_enteros(a, b)`: Retornar la suma de dos números.
> 3) `es_mayor_de_edad(edad)`: Evaluar si es mayor o igual a 18.
> 4) `tipo_de_dato(valor)`: Retornar el nombre del tipo (ej: 'int', 'str') usando `type(valor).__name__`.
> 5) `convertir_a_float(valor)`: Castear un string numérico a tipo float.
> Mostrame el código final limpio sin comentarios innecesarios.

**Resultado obtenido**:

El modelo actuó como tutor y entregó una explicación lógica para cada función (uso de f-strings, el atributo __name__ y casteo de tipos) junto con el bloque de código final compatible con Python 3.13.

**¿Lo usaste tal cual o lo modificaste?**

Lo usé tal cual. El código generado respetaba exactamente los nombres de las funciones y los valores de retorno esperados por los tests de pytest (como los strings de saludo y los nombres de los tipos de datos).
Luego modifiqué la función clasificar numero 0 para que pase el test.

---

### 2 - condicionales.py

**Herramienta**: Gemini 3 Flash

**Prompt usado**:
> Patrón: Interacción Invertida
    Quiero implementar las funciones de condicionales.py. Antes de darme el código, haceme preguntas sobre:

        Cómo clasificar el número 0.

        Los rangos exactos de las notas y si debo agregar validación de errores.

        Si prefiero lógica anidada o compacta para el año bisiesto.

    Mis respuestas fueron:

        El 0 cuenta como positivo.

        Una nota de 6.0 ya es "Bueno" y debo avisar si la nota es inválida (fuera de 0-10).

        Lógica compacta con operadores and/or.

**Resultado obtenido**:

El modelo generó las funciones basadas en mis definiciones específicas, aplicando una estructura de control if/elif/else para las notas y una expresión booleana de una sola línea para el año bisiesto.

**¿Lo usaste tal cual o lo modificaste?**

Lo usé tal cual, aunque verifiqué que el cambio de "Aprobado" por "Bueno" en la nota 6 no rompiera los tests automáticos del repo.
Luego de esto corregí la función de nota aprobado.

---

### 3 - listas.py

**Herramienta**: Gemini 3 Flash

**Prompt usado**:
> Patrón: Verificador Cognitivo
    Estoy por completar src/listas.py. Antes de darme el código, revisá la lógica de estas funciones: suma_lista, filtrar_pares, invertir_lista, eliminar_duplicados y aplanar_lista.

        ¿Qué casos borde debería testear (listas vacías, elementos no numéricos)?

        ¿Cuál es el error más común al intentar invertir una lista o eliminar duplicados?

        Proponé 3 tests para aplanar_lista con diferentes profundidades.
        Luego de este análisis, dame el código final para Python 3.13.

**Resultado obtenido**:

El modelo identificó riesgos como la mutación de listas originales y el manejo de listas vacías (que en sum() devuelven 0). Me propuso usar list comprehensions por eficiencia y el truco de dict.fromkeys para mantener el orden al eliminar duplicados.

**¿Lo usaste tal cual o lo modificaste?**

Lo usé tal cual. Apliqué la técnica de slicing [::-1] para invertir la lista porque es la forma más rápida en Python de crear una copia invertida sin tocar la original.

---

### 4 - diccionarios.py

**Herramienta**: Gemini 3 Flash

**Prompt usado**:
> Actuá como un desarrollador senior de Python. Necesito completar el script diccionarios.py asegurando que pase una suite de tests de pytest. Las funciones son: contar_palabras (debe ser case-insensitive), invertir_diccionario (intercambiar claves por valores), merge_diccionarios (donde d2 debe prevalecer sobre d1 en caso de conflicto) y filtrar_por_valor (debe incluir valores mayores o iguales al mínimo). Utilizá dictionary comprehensions y el operador de desempaquetado para un código limpio y eficiente.

**Resultado obtenido**:

El modelo generó las cuatro funciones solicitadas. Para contar_palabras, se utilizó el método .get() para manejar claves inexistentes de forma segura. Para los filtros e inversiones, se aplicaron comprensiones de diccionarios. Para el merge, se utilizó el operador {**d1, **d2} que garantiza que los valores de d2 sobrescriban a los de d1.

**¿Lo usaste tal cual o lo modificaste?**

Se usó tal cual. La lógica de comparación >= en filtrar_por_valor coincide exactamente con lo requerido por el test test_filtrar_por_valor.

---

### 5 - loops.py

**Herramienta**: Gemini 3 Flash

**Prompt usado**:
> "Actuá como un mentor de programación. Ayudame a resolver el módulo loops.py asegurando que pase todos los tests de pytest. Aplicá el patrón de Cadena de Pensamiento: explicá paso a paso cómo abordar la lógica de es_primo (considerando el caso del 1 y el 2) y cómo generar la serie de fibonacci para que coincida con los tests (empezando en 0). Buscamos soluciones que usen range() y acumuladores de forma eficiente."

**Resultado obtenido**:

Se desglosó la lógica de cada función. Para suma_digitos, se recomendó tratar el número como string para iterar fácilmente. Para fibonacci, se explicó la necesidad de manejar casos base para n=1 y luego usar un bucle que sume los dos últimos elementos. Para es_primo, se estableció que cualquier número menor a 2 no es primo.

**¿Lo usaste tal cual o lo modificaste?**

Se usó tal cual. La lógica de range(1, n + 1) en contar_hasta y el manejo de los primeros 10 múltiplos en tabla_multiplicar se implementaron siguiendo las recomendaciones para que los límites del rango sean exactos.

---

### 6 - funciones.py

**Herramienta**: Gemini 3 Flash

**Prompt usado**:
> "Actuá como un desarrollador senior experto en Programación Funcional. Necesito completar el script funciones.py para que pase una suite de pytest. Las funciones deben implementar: aplicar_funcion (un map manual), componer (retornar una función que aplique f(g(x))), memoizar (usar un closure con un diccionario para cachear resultados) y reducir (un reduce manual sin usar functools). Explicame brevemente la lógica de los closures para asegurar que los tests de estado (como el de memoizar) pasen correctamente."

**Resultado obtenido**:

Se propusieron implementaciones limpias. Para memoizar, se utilizó una función anidada que consulta un diccionario cache definido en el ámbito superior. Para reducir, se utilizó un bucle estándar que actualiza un acumulador partiendo del valor inicial.

**¿Lo usaste tal cual o lo modificaste?**

Se usó tal cual. La implementación de componer respeta estrictamente el orden solicitado en el test: f(g(x)).
---

### 7 - operaciones.py

**Herramienta**: Gemini 3 Flash

**Prompt usado**:
> "Actuá como un desarrollador senior de Python. Necesito completar el módulo operaciones.py siguiendo una serie de tests. La función es_palindromo debe ignorar espacios y mayúsculas. capitalizar_palabras debe poner en mayúscula la primera letra de cada palabra. contar_vocales debe ser case-insensitive. Para caesar_cipher, explicá cómo usar el operador módulo % para que las letras vuelvan al inicio del alfabeto (de 'z' a 'a') manteniendo el caso original y sin alterar símbolos o espacios."

**Resultado obtenido**:

Se generaron las funciones optimizadas. Se destacó que para el cifrado César, la fórmula (ord(c) - base + desplazamiento) % 26 + base es la forma más limpia de manejar el desborde de letras.

**¿Lo usaste tal cual o lo modificaste?**

Se usó tal cual. La implementación de es_palindromo utiliza el reemplazo de espacios y el slicing [::-1] para mayor brevedad y rendimiento.

---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?

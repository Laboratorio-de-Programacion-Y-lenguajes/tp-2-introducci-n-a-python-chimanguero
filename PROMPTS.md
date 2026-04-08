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

---

### 3 - listas.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?

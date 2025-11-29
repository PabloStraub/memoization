# Memoization

Este es un ejemplo de cómo se puede usar memoization para cambiar radicalmente el tiempo de ejecución de una función, 
especialmente cuando ésta tiene múltiples recursiones.

El ejemplo no es original: está tomado de Computerphile en https://youtu.be/JXUOMsFBDXQ?si=h-f46HAjSeXk8IY3.

Explicación del contenido

| Archivo | Explicación |
| ----- | ----- |
| countSteps135.py | Programa que cuenta las formas en que es posible subir una escalera, considerando pasos de 1, 3 y 5 peldaños |
| countSteps.py | Programa que cuenta las formas en que es posible subir una escalera, considerando pasos de distintas cantidades de peldaños, según lista steps |
| countStepsMemoization.py | Versión con memoization de countSteps.py, y por ende muchísimo más eficiente, pero más compleja |
| memoize.py | Definición de la decoración `@memoize` que es específica para los parámetros usados en countSteps.py |
| countStepsMemoize.py | Versión con decoración `@memoize` de countSteps.py, y por ende muchísimo más eficiente, pero simple |
| memoized.py | Definición de la decoración `@memoized` que es genérica porque cualquier lista de parámetros posicionales de tipos inmutables |
| countStepsMemoized.py | Versión con decoración `@memoized` de countSteps.py, y por ende muchísimo más eficiente, pero simple. Acá se usa una tupla para especificar `steps` porque es inmutable. |
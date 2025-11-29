# Memoization

Este es un ejemplo de cómo se puede usar memoization para cambiar radicalmente el tiempo de ejecución de una función, 
especialmente cuando ésta tiene múltiples recursiones.

El ejemplo no es original: está tomado de Computerphile en https://youtu.be/JXUOMsFBDXQ?si=h-f46HAjSeXk8IY3.

Explicación del contenido

| Archivo | Explicación |
| ----- | ----- |
| countSteps135.py | Programa que cuenta las formas en que es posible subir una escalera, considerando pasos de 1, 3 y 5 peldaños |
| countSteps.py | Programa que cuenta las formas en que es posible subir una escalera, considerando pasos de distintas cantidades de peldaños, según lista `steps` |
| countStepsMemoization.py | Versión con memoization de countSteps.py, y por ende muchísimo más eficiente, pero más compleja |
| memoize.py | Definición de la decoración `@memoize` que es específica para los parámetros usados en countSteps.py |
| countStepsMemoize.py | Versión con decoración `@memoize` de countSteps.py, y por ende muchísimo más eficiente, pero simple |
| memoized.py | Definición de la decoración `@memoized` que es genérica porque cualquier lista de parámetros posicionales de tipos inmutables |
| countStepsMemoized.py | Versión con decoración `@memoized` de countSteps.py, y por ende muchísimo más eficiente, pero simple. Acá se usa una tupla para especificar `steps` porque es inmutable. |

## Análisis de tiempo de ejecución de count_steps_135

Considera la versión count_steps_135 del módulo countSteps.py.

Supongamos que cada operación simple toma la misma cantidad de tiempo. Entonces lo que debemos hacer es contar la cantidad de operaciones simples. 

Para `n` igual a cero se necesitan dos unidades de tiempo (if y return). Para `n` menor que cero se necesitan 3 unidades de tiempo (un if falso, un if verdadero y return).

Para `n` mayor que 0 es un poco más complejo. Se necesitan dos if falsos, tres llamados a función, tres restas, dos sumas y el costo de las funciones con `n`-1, `n`-3 y `n`-5.

En resumen, la cantidad de operaciones está dada por la siguiente función:
```
f(0) = 2
f(n) = 3, si n < 0
f(n) = 10 + f(n-1) + f(n-3) + f(n-5), si n > 0
```

El programa f_345.py computa esta función `f`, obviamente usando `@memoized` porque en caso contrario demoraría mucho.

| n | f(n) | Factor
| ---- | ---- | ---- |
|  -5 | 3 |     1.0 |
|   0 | 2 |   0.667 |
|   5 | 126 |    63.0 |
|  10 | 1,268 |    10.1 |
|  15 | 12,146 |    9.58 |
|  20 | 115,958 |    9.55 |
|  25 | 1,106,678 |    9.54 |
|  30 | 10,561,490 |    9.54 |
|  35 | 100,792,306 |    9.54 |
|  40 | 961,898,840 |    9.54 |
|  45 | 9,179,761,618 |    9.54 |
|  50 | 87,605,909,802 |    9.54 |
|  55 | 836,056,070,762 |    9.54 |

Se ve que para `n` igual a 40 se tiene casi mil millones de operaciones. Y para `n` grandes, en la medida que se *suma* 5 a `n` la cantidad de operaciones se *multiplica* por 9,54.
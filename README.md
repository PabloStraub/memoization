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

Considera la versión `count_steps_135` del módulo countSteps.py.

Supongamos que cada operación simple toma la misma cantidad de tiempo. Entonces lo que debemos hacer es contar la cantidad de operaciones simples. 

Para `n` igual a cero se necesitan dos unidades de tiempo (if y return). Para `n` menor que cero se necesitan 3 operaciones (un if falso, un if verdadero y return).

Para `n` mayor que 0 es un poco más complejo. Se necesitan dos if falsos, tres llamados a función, tres restas, dos sumas, un return y el costo de las funciones con `n`-1, `n`-3 y `n`-5.

En resumen, la cantidad de operaciones está dada por la siguiente función:
```
f(0) = 2
f(n) = 3, si n < 0
f(n) = 11 + f(n-1) + f(n-3) + f(n-5), si n > 0
```

El programa f_345.py computa esta función `f`, obviamente usando `@memoized` porque en caso contrario demoraría mucho.

| n | f(n) | Factor |
| ---- | ---- | ---- |
|  -5 | 3 |     1.0 |
|   0 | 2 |   0.667 |
|   5 | 134 |    67.0 |
|  10 | 1,350 |    10.1 |
|  15 | 12,933 |    9.58 |
|  20 | 123,473 |    9.55 |
|  25 | 1,178,401 |    9.54 |
|  30 | 11,245,974 |    9.54 |
|  35 | 107,324,598 |    9.54 |
|  40 | 1,024,238,958 |    9.54 |
|  45 | 9,774,696,761 |    9.54 |
|  50 | 93,283,599,121 |    9.54 |
|  55 | 890,240,390,449 |    9.54 |
|  60 | 8,495,898,102,314 |    9.54 |
|  65 | 81,079,543,614,214 |    9.54 |
|  70 | 773,772,509,217,750 |    9.54 |
|  75 | 7,384,401,407,954,381 |    9.54 |
|  80 | 70,472,113,578,867,185 |    9.54 |
|  85 | 672,541,824,029,649,825 |    9.54 |

Se ve que para `n` igual a 40 se tiene casi mil millones de operaciones. Con `n` igual a 55 se acerca al billón de operaciones (*trillion*, en inglés). Y en general, para `n` grandes, en la medida que se *suma* 5 a `n` la cantidad de operaciones se *multiplica* por 9,54.

Para valores de `n` grandes esta función se puede aproximar por:

```LaTeX
\[
f(n) \approx 9.61 \cdot (1.570322)^n - 5.5.
\]
```
Esto muestra claramente la naturaleza exponencial del algoritmo, lo que hace imposible usarlo con valores de `n` grandes.

# Análisis de countStepsMemoization

Analicemos ahora countStepsMemoization. Para simplificar, vamos a restringir el análisis a la situación donde el primer elemento de `steps` es 1.

Considera la línea 8 de `countStepsMemoization.py`

```python
    result = sum(count_steps(n - step, steps, memo) for step in steps)
```

Para efectos de análisis vamos a suponer que esto se ejecuta como si estuviera escrito así:

```python
    result = 0
    for step in steps:
        result += count_steps(n - step, steps, memo)
```

Si consideramos que `steps[0]` es 1, entonces la primera iteración va a computar los valores de `count_steps` para todos los números menores que n. Esto es debido a que lo primero que hace es computar `count_steps(n - 1, steps, memo)` pero este cómputo lo primero que hará es computar `count_steps(n - 2, steps, memo)` y así sucesivamente hasta llegar a `n` igual a cero.

Entonces los siguientes cómputos para otros valores de `step` estarán todos almacenados en `memo`.

Considerando lo anterior, podemos contar la cantidad de operaciones en forma similar a como lo hicimos con `count_steps_135`. 

Para `n` igual a cero se necesitan dos unidades de tiempo (if y return). Para `n` menor que cero se necesitan 3 operaciones (un if falso, un if verdadero y return). Esta parte es igual al caso sin memoization.

Para `n` mayor que 0, donde el dato está precomputado en `memo`, se necesitan 6 operaciones: 2 if falsos, 1 acceso a `memo`, 1 if verdadero, 1 acceso a `memo[n]`, 1 return.

Para `n` mayor que 0, pero donde el dato está no precomputado en `memo`, se necesita primero llegar al inicio de la iteración, con 5 operaciones: 2 if falsos, 1 acceso a `memo`, 1 if falso, 1 inicializar `result`. Luego en la primera iteración (donde suponemos que `steps[0]` es 1) hay 1 acceso a `steps`, 1 resta, 1 llamado a `count_steps`, 1 suma a `result`. Es decir tenemos 4 operaciones adicionales, más todas las operaciones que se necesiten para computar `count_steps(n - step, steps, memo)`. Pero ahora nos falta sumar las operaciones de todos las otras iteraciones; es decir, faltan `len(steps) - 1` iteraciones. Cada iteración tendrá: un acceso a steps, una suma, un llamado a count_steps que usa `memo` (recordemos que eso son 6 operaciones), en total son 9 operaciones.

En resumen, la cantidad de operaciones está dada por la siguiente función:
```
m(0) = 2
m(n) = 3, si n < 0
m(n) = 8 + f(n-1) + 9 * ls, si n > 0
```

Donde ls es `len(steps) - 1`, en nuestro caso ls = 2.

Simplificando e ignorando el caso de los número negativos, tenemos:

```
m(0) = 2
m(n) = 26 + f(n-1), si n > 0
```
Es fácil demostrar que `m(n) = 2 + 26 n`. Esto explica por qué el cómputo es tan rápido aún con n relativamente grande.

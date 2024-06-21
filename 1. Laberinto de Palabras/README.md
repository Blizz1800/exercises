# Reto de programación: Laberinto de Palabras

## Descripción

Crea un programa que genere un laberinto de letras aleatorias y luego determine si una palabra dada se puede encontrar dentro del laberinto, letras adyacentes (horizontal o verticalmente, no en diagonal).

## Datos

### Entrada

1. Un número entero `n` que representa el tamaño del laberinto (`n * n`).
2. Una palabra a buscar dentro del laberinto.

### Salida

`True` si la palabra se encuentra en el laberinto, `False` en caso contrario.

## Ejemplo

```stdout
$ Tamanno del laberinto: 5
$ Palabra a buscar: hOlA

R A N D O
H O L A M
Z C V B N
P Q W E R
T Y U I O

Se ha encontrado la palabra
```

## Puntos extra

* [x] Imprime el laberinto generado en la consola.

* [x] Si la palabra se encuentra, resalta el camino de la palabra en el laberinto.

* [x] Permite al usuario ingresar el tamaño del laberinto y la palabra a buscar.

* [ ] Implementa diferentes algoritmos de búsqueda de palabras (por ejemplo, búsqueda en profundidad, búsqueda en amplitud).

## Pistas

* Puedes representar el laberinto como una matriz de caracteres.
* Para generar letras aleatorias, puedes usar la función `random.choice(string.ascii_uppercase)`.
* Para buscar la palabra en el laberinto, puedes usar un algoritmo de búsqueda recursiva o iterativa.

¡Diviértete programando!

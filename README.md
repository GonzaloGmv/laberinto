# laberinto

Mi dirección de github para este repositorio es: [ github](https://github.com/GonzaloGmv/laberinto)

He realizado un programa para realizar un laberinto a partir de una lista, y además he realizadoo otro programa que resuelve este laberinto. En la primera parte he hecho un bucle para que se añada una "X" en el lugar donde dice la lista. Para realizar el segundo programa he utilizado el primero, a través de un módulo, para construir el laberinto a resolver. Después he creado las variables **i** y **j** para la posición en cada momento, y las variables **k** y **l** para la posición anterior. Usando estas variables, he hecho un bucle en el que había condicionales para comprobar si había un muro, "X", a la derecha, izquierda, abajo o arriba, y de esta forma, se iba hacia donde no hubiera muro. Lo de la posición anterior , **k** y **l**, lo he añadido para que el programa comprobara de dónde venía y que no volviera hacia esa dirección, y de esta manera evitar el bucle infinito.

Mi **diagrama de flujo** para este proyecto es:

![diagrama_laberinto](https://user-images.githubusercontent.com/91721237/144579055-64e4399b-2404-48de-b072-cfc3571e5904.jpg)

El código de este proyecto es el siguiente:

#### Tarea 1
```
def tablero(LABERINTO):

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

for i in range (12):
    LABERINTO[muro[i][0]][muro[i][1]] = "X"

for i in range (5):
    print(LABERINTO[i])
```
#### Tarea 2
```
import tarea1
print("Este es nuestro laberinto: ")
laberinto = [
        ['E', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', ' '], 
        [' ', ' ', ' ', ' ', 'S']
    ]
tarea1.tablero(laberinto)

i = 0
j = 0
k = 0
l = 0
instrucciones = list('')

while laberinto[i][j] != 'S':
    if i < 4 and i >= k and laberinto[j][i+1] != 'X':
        instrucciones.append("Derecha")
        i = i + 1
        k = i - 1
        l = j
    elif i > 0 and i < k and laberinto[j][i-1] != 'X':
        instrucciones.append("Izquierda")
        i = i - 1
        k = i + i
        l = j
    elif j < 4 and j >= l and laberinto [j+1][i] != 'X':
        instrucciones.append("Abajo")
        j = j + 1
        l = j - 1
        k = i
    else:
        instrucciones.append("Arriba")
        j = j - 1
        l = j + 1
        k = i
print("Asi es como se sale del laberinto: ")
print(instrucciones)
```

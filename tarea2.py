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
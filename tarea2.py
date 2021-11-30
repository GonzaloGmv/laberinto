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
instrucciones = list('')

while laberinto[i][j] != 'S':
    if i < 4 and laberinto[j][i+1] != 'X':
        instrucciones.append("Derecha")
        i = i + 1
        k = j
    elif j >= k and laberinto [j+1][i] != 'X':
        instrucciones.append("Abajo")
        j = j + 1
        k = j - 1
    else:
        instrucciones.append("Arriba")
        j = j - 1
        k = j + 1
print("Asi es como se sale del laberinto: ")
print(instrucciones)
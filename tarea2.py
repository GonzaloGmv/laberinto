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
while i < 5 and j < 5:
    if i < 4 and laberinto[j][i+1] != 'X':
        print("Derecha")
        i = i + 1
        k = j
    elif j >= k and laberinto [j+1][i] != 'X':
        print("Abajo")
        j = j + 1
        k = j - 1
    else:
        print("Arriba")
        j = j - 1
        k = j + 1
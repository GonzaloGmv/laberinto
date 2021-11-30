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
while i < 5:
    if laberinto[j][i+1] != 'X' and i < 4:
        print("Derecha")
        i = i + 1
    elif laberinto [j+1][i] != 'X' and j >= k:
        print("Abajo")
        j = j + 1
        k = j - 1
    else:
        print("Arriba")
        j = j - 1
        k = j + 1
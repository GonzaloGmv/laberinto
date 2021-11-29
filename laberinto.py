laberinto = [
    [' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' ', 'S']
]

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

laberinto[muro[0][0]][muro[0][1]] = "X"
laberinto[muro[1][0]][muro[1][1]] = "X"
laberinto[muro[2][0]][muro[2][1]] = "X"
laberinto[muro[3][0]][muro[3][1]] = "X"
laberinto[muro[4][0]][muro[4][1]] = "X"
laberinto[muro[5][0]][muro[5][1]] = "X"
laberinto[muro[6][0]][muro[6][1]] = "X"
laberinto[muro[7][0]][muro[7][1]] = "X"
laberinto[muro[8][0]][muro[8][1]] = "X"
laberinto[muro[9][0]][muro[9][1]] = "X"
laberinto[muro[10][0]][muro[10][1]] = "X"
laberinto[muro[11][0]][muro[11][1]] = "X"

print(laberinto[0])
print(laberinto[1])
print(laberinto[2])
print(laberinto[3])
print(laberinto[4])
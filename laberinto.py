entrada = "E"
pared = "X"
espacio = " "
salida = "S"
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0),
(4,1), (4,2), (4,3))
empezar = (0,0)
acabar = (4,4)
fila = 0
columna = 0
movimientos = 0

laberinto = [
    ['E', 'X', 'X', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    ['X', 'X', 'X', 'X', 'S']
]
for i in laberinto:
    print(i)

def recorrido(tablero):
    mov = ['Abajo', 'Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Arriba', 'Arriba', 'Derecha', 'Derecha', 'Abajo', 'Abajo', 'Abajo']
    n = 0
    m = 0
    while (fila < 1 and columna < 1):   
                if k <= n < 4 and laberinto[m][n+1] != 'X':   
                        movimientos.append("Derecha")
                        n += 1
                        k = n-1
                        l = m
                elif 0 < n < k and laberinto[m][n-1] != 'X':   
                        movimientos.append("Izquierda")
                        n -= 1
                        k = n+1
                        l = n
                elif l <= m < 4 and laberinto[m+1][n] != 'X':  
                        movimientos.append("Abajo")
                        m += 1
                        l = m - 1
                        k = n
                else:   
                        movimientos.append("Arriba")
                        m -= 1
                        l = m + 1
                        k = n
print("Final del laberinto")
return movimientos


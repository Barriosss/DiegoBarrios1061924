# Crear el tablero de ajedrez vacío
tablero = [[" " for _ in range(8)] for _ in range(8)]
# Lista de letras para las columnas del tablero
columnas = ["a", "b", "c", "d", "e", "f", "g", "h"]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("  a b c d e f g h")
    for i in range(8):
        print(8 - i, end=" ")
        for j in range(8):  
            print(tablero[i][j], end=" ")
        print(" " + str(8 - i))
    print("  a b c d e f g h")

# Función para convertir coordenadas en formato 'letra número' a índices de matriz
def coordenada_a_indices(coordenada):
    columna = columnas.index(coordenada[0].lower())
    fila = 8 - int(coordenada[1])
    return fila, columna

# Función para convertir índices de matriz a coordenadas en formato 'letra número'
def indices_a_coordenada(fila, columna):
    return columnas[columna] + str(8 - fila)

# Preguntar si se desean ingresar piezas al tablero
while True:
    respuesta = input("¿Desea ingresar piezas al tablero? (si/no): ").strip().lower()
    if respuesta == "no":
        break
    elif respuesta == "si":
        # Preguntar por el tipo de pieza
        tipo_pieza = input("Ingrese el tipo de pieza (torre, rey, reina, alfil, peón, caballo): ").strip().lower()
        # Preguntar por el color de la pieza
        color_pieza = input("Ingrese el color de la pieza (b para blanco, n para negro): ").strip().lower()
        # Preguntar por la coordenada de la pieza
        coordenada = input("Ingrese la coordenada de la pieza (ej. e4): ").strip().lower()
        fila, columna = coordenada_a_indices(coordenada)
        # Agregar la pieza al tablero
        tablero[fila][columna] = tipo_pieza[0].upper() + color_pieza.upper()
        # Si se agregó una torre, terminar el ciclo
        if tipo_pieza == "torre":
            break
    else:
        print("Respuesta no válida. Por favor, ingrese 'si' o 'no'.")

# Imprimir el tablero con las piezas ingresadas
print("\nTablero actual:")
imprimir_tablero(tablero)

# Imprimir las posiciones de las piezas ingresadas
print("\nPosiciones de las piezas ingresadas:")
for i in range(8):
    for j in range(8):
        if tablero[i][j] != " ":
            print(f"Pieza: {tablero[i][j]} en {indices_a_coordenada(i, j)}")

# Si se ingresó una torre, mostrar las posiciones donde puede moverse
if tipo_pieza == "torre":
    print("\nPosiciones posibles para la torre:")
    # Evaluar movimientos verticales y horizontales
    torre_color = tablero[fila][columna][1]
    # Movimiento vertical hacia arriba
    for i in range(fila - 1, -1, -1):
        if tablero[i][columna] == " " or tablero[i][columna][1] == torre_color:
            print(indices_a_coordenada(i, columna))
        else:           
            continue
    # Movimiento vertical hacia abajo
    for i in range(fila + 1, 8):
        if tablero[i][columna] == " " or tablero[i][columna][1] == torre_color:
            print(indices_a_coordenada(i, columna))
        else:
            continue
    # Movimiento horizontal hacia la izquierda
    for j in range(columna - 1, -1, -1):
        if tablero[fila][j] == " " or tablero[fila][j][1] == torre_color:
            print(indices_a_coordenada(fila, j))
        else:
            continue
    # Movimiento horizontal hacia la derecha
    for j in range(columna + 1, 8):
        if tablero[fila][j] == " " or tablero[fila][j][1] == torre_color:
            print(indices_a_coordenada(fila, j))
        else:
            continue
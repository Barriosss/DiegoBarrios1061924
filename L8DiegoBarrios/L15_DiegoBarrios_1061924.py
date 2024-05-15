#ACTVIDAD1
#Diego Alexander Barrios Rivas 1061924
def obtener_area_triangulo(b, h):
    area =(b * h) / 2
    return area

def obtener_area_cuadrado(l):
    area = l ** 2
    return area

def obtener_area_rectangulo(b, h):
    area = b * h
    return area

def obtener_area_circulo(r):
    area = 3.1416 * r ** 2
    return area

def menu():
    print("1. Calcular área de un triángulo")
    print("2. Calcular área de un cuadrado")
    print("3. Calcular área de un rectángulo")
    print("4. Calcular área de un círculo")
    opcion = int(input("Seleccione una opción (1-4): "))
    match (opcion):
        case 1:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = obtener_area_triangulo(base, altura)
            print("El área del triángulo es:", area)
        case 2:
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = obtener_area_cuadrado(lado)
            print("El área del cuadrado es:", area)
        case 3:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = obtener_area_rectangulo(base, altura)
            print("El área del rectángulo es:", area)
        case 4:
            radio = float(input("Ingrese el radio del círculo: "))
            area = obtener_area_circulo(radio)
            print("El área del círculo es:", area)
        case _:
            print("Opción no válida")

menu()


#ACTIVIDAD 2
#DIEGO ALEXANDER BARRIOS RIVAS 1061924
x = 0 
y = 0

#declaración de función, se utiliza la palabra "def" nombre de la función y entre () van los parametros o las entradas de la misma
def MoverPosicion(cantX, cantY):
    global x, y 
    x += cantX
    y += cantY

#Ciclo while para desplegar el menú de opciones
opcion = 'a'
while(opcion != 'e'):
    print("Menú")
    print("a. Sube","b. Baja","c. Izquierda","d. Derecha", "e. Salir", sep = "\t\n")
    opcion = input("ingrese su opción: ")

    match opcion:
        case 'a': #opción sube
            MoverPosicion(0,1) #para cada opción se manda a llamar la función creada anteriormente
        case 'b': #opción baja
            MoverPosicion(0,-1)
        case 'c':
            MoverPosicion(-1,0)
        case 'd':
            MoverPosicion(1,0)

    print(f"La poscición actual es: [{x}][{y}]")

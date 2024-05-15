import random 
print ("Semana No.16: Ejercicio 1")
lista= []
for x in range (10):
    lista.append(random.randint(0,10))

opcion= 'a'

while (opcion != 'e'):
    print ("Menú")
    print("a. Mostrar números ingresados \n", "b. Promedio \n" , "c. Longitud \n", "d. Suma posiciones impares y pares" )
    opcion = str(input("Digite opción a reaizar: \n"))

    match opcion:
        case 'a':
            for x in range (len(lista)):
                print(f"No. {x}: {lista[x]}")
        case 'b':
            print ("PROMEDIO")
            suma=0
            for x in range (len(lista)):
                suma+= lista[x]
            promedio = suma / len(lista)
            print (f"----Promedio: {promedio}")

        case 'c': 
            print ("LONGITUD")
            for x in range (len(lista)):
                print (len[lista])
        
        case 'd':
            sumapar= 0
            sumaimpar=0
            print("SUMA PARES IMPARES")
            for x in range (len(lista)):
                if (x % 2 == 0):
                    sumapar+= lista[x]
                else:
                    sumaimpar+= lista[x]

            print (f"Suma números pares: {sumapar}")
            print (f"Suma números impares: {sumaimpar}")

print ("EJERCICIO 2")

cantFilas = int(input("Ingrese la cantidad de filas: "))
cantCols = int(input("Ingrese la cantidad de columnas: "))

matriz = [[0 for x in range(cantCols)] for y in range(cantFilas)]
mayor = 0
sumaPARES=0
SumaIMPARES=0
menor=1000
for xFilas in range(cantFilas):
    for xCols in range(cantCols):
        matriz[xFilas][xCols] = random.randint(0, 1000)
        if (matriz[xFilas][xCols]% 2 ==0):
            sumaPARES+=matriz[xFilas][xCols]
        else:
            SumaIMPARES+=matriz[xFilas][xCols]

        if(matriz[xFilas][xCols] > mayor):
            mayor = matriz[xFilas][xCols]

        if(matriz[xFilas][xCols] < menor):
            menor = matriz[xFilas][xCols]

print(matriz)
print(f"El numero mayor es: {mayor}")
print(f"El número menor es: {menor}")
print(f"La suma de números pares: {sumaPARES}")
print(f"La suma de números impares: {SumaIMPARES}")



#EJE1
print ("EJERCICIO 1")
num1=int(input("Ingrese un número \n "))
num2=int(input("Ingrese un número mayor al primero \n "))

def primosRango(num1, num2):
    primosDEF=[]
    for num in range (num1, num2+1):
        if num > 1:
            esprimo=True
        for i in range (2, num):
            if (num % i) == 0:
                esprimo= False
                break
        if esprimo==True:
            primosDEF.append(num)
    return primosDEF
primoss= primosRango(num1, num2)
print ("Números primos en el rango: ", primoss, "\n")

#EJE2
print("EJERCICIO 2")
def es_palindromo(frase):
    frase= frase.lower()
    frase= frase.replace(" ", "")
    frase= frase.replace("á", "a")
    frase= frase.replace("é", "e")
    frase= frase.replace("í", "i")
    frase= frase.replace("ó", "o")
    frase= frase.replace("ú", "u")

    a= 0
    b= len(frase) -1

    for i in range (0, len(frase)):
        if frase[a] == frase[b]:
            a += 1
            b -= 1
        else:
            return False
    return True

frase = str(input("Ingrese una frase: "))
if (es_palindromo(frase)):
    print("Frase políndroma!")
else:
    print ("No es una frase políndroma :( \n")

#EJE3
print("EJERCICIO 3")
def numeros_arreglos(arreglo, num):
    if (num == sum(arreglo) or num in arreglo):
        return True
    else:
        return False

arreglo= [int(x) for x in frase.split()]
num = int(input("Ingrese un número: "))

res= numeros_arreglos(arreglo, num)
if res:
    print(f"El número {num} es igual a la sumatoria de los valores del arreglo")
else:
     print(f"El número {num} no es igual a la sumatoria de los valores del arreglo \n")

#EJE4
print("EJERCICIO 4")
cadena2=str(input("Ingrese un conjunto de caracteres en forma de oración:\n"))
print("Su oracion es:\n", cadena2)
def dentroDe(cadena1, cadena2):
    tamaño=len(cadena1)-1
    tamaño2=len(cadena2)-1
    for i in range (0, tamaño2,1):
        if cadena1[0:tamaño] == cadena2[i:tamaño2]:
            print("Su palabra se encuentra en la oracion")
            return
    print("Su palabra no esta en la frase")








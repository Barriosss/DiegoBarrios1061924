print ("Ejercicio 1")

n1 = int(input("Ingrese el primer número: "));
n2 = int(input("Ingrese el segundo número: "));

divisionR = n1/n2
divisionE = n1 // n2
divisionM = n1 % n2
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2

print ("La división real se representa por: ", n1, " / ", n2, " = ", divisionR)
print ("La división Entera se representa por: ",n1, " // ", n2, "=", divisionE)
print ("La división Modular se representa por: ",n1, " % ", n2, "=", divisionM)
print ("La suma se representa por: ",n1, " + ", n2, "=", suma)
print ("La resta real se representa por: ",n1, " - ", n2, "=", resta)
print ("La multiplicación se representa por: ",n1, " * ", n2, "=", multiplicacion)
 
"\n"

print ("Operaciones Booleanas")

igualdad = n1 == n2
diferencia = n1 != n2
mayor = n1 > n2
menor = n1 < n2

print (n1, " == ", n2, "=", igualdad)
print (n1, " != ", n2, "=", diferencia)
print (n1, " > ", n2, "=", mayor)
print (n1, " < ", n2, "=", menor)

"\n"

print ("Jerarquía de operaciones")
a = int(input("Ingrese el primer número: "));
b = int(input("Ingrese el segundo número: "));
c = int(input("Ingrese el tercer número: "));

print ("i. ", (a*b)+c)
print ("ii. ", a*(b+c))
print ("iii. ", a / (b+c))
print ("IV. ", ((3*a) + (2*b)) / pow (c, 2))

print ("Ejercicio 4:  Conversión de medidas")
metros1= int(input("Ingrese metros: "))

km= metros1 / 1000
Millas = km / 1.69
Pies = metros1 * 3.28
Pulgadas = Pies * 12

print ("Km: ", km)
print ("Millas: ", Millas)
print ("Pies: ", Pies)
print ("Pulgadas: ", Pulgadas)

print ("Actividad 3 ejercicio final")
metros2 = float (input("Digite metros a convertir: "))

yardas = metros2 // 0.9144
modYardas = metros2 % 0.9144
pies = modYardas // 0.333333
modPies= metros2 % 0.333333
pulgadas = modPies // 0.0833333


print ("Yardas: ", yardas, "Pies: ", pies, "Pulgadas: ", pulgadas)


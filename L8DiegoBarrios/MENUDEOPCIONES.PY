print ("Presione el número correspondiente a la actividad que desea realizar:  \n")
print ("1. Ver si un número es par o impar \n")
print ("2. Indicar si un número es múltiplo de 5 \n")
print ("3. Devolver la calificación con letra de los siguientes rangos: \n")
print ("- Menor a 50 = F \n")
print ("- 50 y 60 = D \n")
print ("- 60 y 70 = C \n")
print ("- 70 y 85 = B \n")
print ("- Mayor a 85 = A \n")
print ("4. Calcular hipotenusa a partir de dos catetos: \n")

Resultado= int(input("Digite un número para realizar la acción: "))

match (Resultado): 
    case 1:
        num1= int (input("Digite un número: "))
        if num1 % 2 == 0:
            print ("El número es par")
        else: 
            print ("El número es impar")
    case 2:
        num2= int(input("Digite un número para la acción: "))
        if num2 % 5 == 0:
            print ("El número es múltiplo de 5")
        else:
            print("El número no es múltiplo de 5")
    case 3:
        nota= int (input("Digite su nota de 1-100: "))
        if nota < 50:
            print ("Nota F")
        elif nota <= 50 and nota <= 60:
            print ("Nota D")
        elif nota < 60 and nota <= 70:
            print ("Nota C")
        elif nota < 70 and nota <= 85:
            print ("Nota B")
        else:
            print("Nota A")
    case 4:
        cateto1= float (input("Digite cateto 1 para calcular la hipotenusa: "))
        cateto2 = float(input("Digite cateto 2 para calcular la hipotesua: "))

        suma= [pow (cateto1, 2)] + [pow (cateto2, 2)]
    

        print (res)





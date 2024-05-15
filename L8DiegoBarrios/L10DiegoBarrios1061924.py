print ("Semana No. 10: Ejercicio 1")
mesEntrada= int(input("Ingrese un número del 1-12: "))
mesSalida= ""

match mesEntrada:
    case 1:
        mesSalida="Enero"
    case 2:
        mesSalida="Febrero" 
    case 3:
        mesSalida="Marzo" 
    case 4:
        mesSalida="Abril" 
    case 5:
        mesSalida="Mayo" 
    case 6:
        mesSalida="Junio" 
    case 7:
        mesSalida="Julio" 
    case 8:
        mesSalida="Agosto" 
    case 9:
        mesSalida="Septiembre" 
    case 10:
        mesSalida="Octubre"
    case 11:
        mesSalida="Noviembre" 
    case 12:
        mesSalida="Diciembre"
    case _:
        mesSalida="Error al encontrar mes, intentelo de nuevo!!"

print (mesSalida) 

"\n"

#ACTIVIDAD 2
print ("SEMANA 10 EJERICIO 2")

a = int(input("Ingrese primer número mayor a 0: "))
b = int(input("Ingrese segundo número mayor a 0: "))
c = int(input("Ingrese tercer número mayor a 0: "))

if (a <= 0 or b <= 0 or c<=0):
    print ("Error: El número debe de ser mayor a 0")

if (a > b):
    if (a < c):
        print ("El númeor mayor es: ", a)
    else:
        if (a == c):
            print ("Los número mayores son: ", a, " y ", c)
        else:
            print ("El número mayor es: ", c)
else:
    if (a == b):
        if (a > c):
            print ("Los número mayores son: ", a, " y ", b)
        else:
            if (a == c):
                print ("Los tres números son iguales")
            else:
                print ("El mayor es: ", c)
    else:
        if (b > c):
            print ("El número mayor es: ", b)
        else:
            if (b == c):
                print ("Los números mayores son: ", b, " y ", c)
            else:
                print("El número mayor es: ", c)

#ACTIVIDAD 3
print ("ACTIVIDAD 3")

DIA = int(input("Ingrese su día de nacimiento "))
MES = int(input("Ingrese su mes de nacimiento "))

match MES:
    case 1:
        if (DIA<=19):
            print("Capricornio")
        else: 
            print("Acuario")
    case 2:
        if (DIA<=18):
            print("Acuario")
        else: 
            print("Piscis")
    case 3:
        if (DIA<=20):
            print("Piscis")
        else: 
            print("Aries")
    case 4:
        if (DIA<=19):
            print("Aries")
        else: 
            print("Tauro")
    case 5:
        if (DIA<=20):
            print("Tauro")
        else: 
            print("Géminis")
    case 6:
        if (DIA<=20):
            print("Géminis")
        else: 
            print("Cáncer")
    case 7:
        if (DIA<=22):
            print("Cáncer")
        else: 
            print("Leo")
    case 8:
        if (DIA<=22):
            print("Leo")
        else: 
            print("Virgo")
    case 9:
        if (DIA<=22):
            print("Virgo")
        else: 
            print("Libra")
    case 10:
        if (DIA<=22):
            print("Libra")
        else: 
            print("Escorpio")
    case 11:
        if (DIA<=21):
            print("Escorpio")
        else: 
            print("Sagitario")
    case 12:
        if (DIA<=21):
            print("Sagitario")
        else: 
            print("Capricornio")





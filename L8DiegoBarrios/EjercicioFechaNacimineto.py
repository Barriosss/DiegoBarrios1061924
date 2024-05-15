import datetime
fecha_actual = datetime.datetime.now()

AÑOActual = fecha_actual.year
MESActual = fecha_actual.month
DÍAactual = fecha_actual.day

Escribir = 'Ingrese su fecha de nacimiento: \n'
print (Escribir)
día= int(input("Digite día de nacimiento: "))
mes = int(input("Digite mes de nacimiento: "))
año = int(input("Digite año de nacimiento: "))

age = AÑOActual - año

if (AÑOActual < año):
    print("Usted aún no nace!")
elif (AÑOActual == año):

    if (mes > MESActual):
     print("Usted aún no nace!")

    elif (mes == MESActual):
       if  (DÍAactual < día):
          print ("Usted aún no nace!")
    else:
       print ("TIENE CERO AÑOS!")
else:
   if (mes == MESActual) and (día > DÍAactual) or (mes > MESActual):
      age = age - 1
print ("Usted tiene ", age, "años")
if (AÑOActual == año) and (MESActual == mes) and (DÍAactual == día):
   print ("Feliz cumpleaños!!")

      
       
       
       
    


















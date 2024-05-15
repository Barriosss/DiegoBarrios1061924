print ("Bienvenido al programa!")
print ("Datos generales (Campos OBLIGATORIOS) ")
nombre= str(input("Nombre Completo: "))
edad = int(input("Escribe tu edad: "))
print ("¿Cuál es tu color favorito? \n")
print ("1. Rojo \n")
print ("2. Anaranjado \n")
print ("3. Amarillo \n")
print ("4. Azul \n")
print ("5. Verde \n")
color = int (input("Elige el color mediante el número: "))

#Importar turtle a python
import turtle

#Ejemplo de dibujar un cuadrado utilizando el ciclo for
turtle.teleport (-300, 275)
for x in range(0, 2):
    turtle.forward(600)
    turtle.left(90)
    for x in range (2,3):
        turtle.forward(-50)
        turtle.left(90)
turtle.penup()
turtle.forward(150)  
turtle.left(-90)
turtle.forward(30)  
turtle.write("Titulo escena 1: El Comienzo", font=("Arial", 16, "bold"))
turtle.hideturtle()

turtle.pendown()
turtle.teleport(300,-250)
for x in range(0, 2):
    turtle.forward(-100)
    turtle.left(90)
    for x in range (2,3):
        turtle.forward(-600)
        turtle.left(90)
turtle.penup()
turtle.forward(-75)  
turtle.left(-90)
turtle.forward(590)
turtle.write("Nombre: "+ nombre)
turtle.goto(turtle.xcor(), turtle.ycor() - 20) 
turtle.write("Edad: "+ edad)
turtle.goto(turtle.xcor(), turtle.ycor() - 20) 
turtle.write("En un bosque muy lejano llamado Bosque Encantado, vivía una ardilla traviesa llama-", font=("Arial", 12))
turtle.goto(turtle.xcor(), turtle.ycor() - 20) 
turtle.write("da Cuki. Cuki era conocida por su curiosidad y su amor por las aventuras. Un día,", font=("Arial", 12))
turtle.goto(turtle.xcor(), turtle.ycor() - 20) 
turtle.write("mientras saltaba de rama en rama, encontró un mapa antiguo entre las hojas secas.", font=("Arial", 12))
turtle.hideturtle()

turtle.pendown()
turtle.teleport (-300, 225)
for x in range(0, 2):
    turtle.forward(-600)
    turtle.left(-90)
    for x in range (2,3):
        turtle.forward(-375)
        turtle.left(-90)


turtle.done()



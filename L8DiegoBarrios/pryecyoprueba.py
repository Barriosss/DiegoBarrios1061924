print ("Bienvenido al programa!")
print ("Datos generales (Campos OBLIGATORIOS) ")
nombre= str(input("Nombre Completo: "))
edad = str(input("Escribe tu edad: "))
print ("¿Cuál es tu color favorito? \n")
print ("1. Rojo \n")
print ("2. Anaranjado \n")
print ("3. Amarillo \n")
print ("4. Azul \n")
print ("5. Verde \n")
color = int (input("Elige el color mediante el número: "))

import turtle

turtle.pendown()
turtle.teleport(-300,170)
for x in range(0, 2):
    turtle.forward(600)
    turtle.left(-90)
    for x in range (2,3):
        turtle.forward(300)
        turtle.left(-90)
turtle.penup()
turtle.forward(135)  
turtle.left(-90)
turtle.forward(50)
turtle.color("brown")  
turtle.write("BIENVENIDO "+ nombre + "!!!", font=("Arial", 20, "bold"))
turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
turtle.write("Edad: " + edad, font=("Arial", 12))
turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
turtle.write("Que empiece el cuento :D. Presione espacio", font=("Arial", 12))  
turtle.hideturtle()

def cambiar_escena_inicio():
    turtle.write("", align="center", font=("Arial", 14, "bold"))

    numero_escena = turtle.textinput("AVISOOOOO!", "Desea iniciar? Presione 00")

    try:
        numero_escena = int (numero_escena) 
        print(f"Cambiando a la escena...")  
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

    if (numero_escena==00):
        escena= int(turtle.textinput("Coloque la escena a la que quiere trasladarse","5 escenas disponibles"))
        match (escena):
            case 1:
                turtle.clear()
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

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                    numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                    try:
                        numero_escena = int (numero_escena) 
                        print(f"Cambiando a la escena...")  
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número válido.")

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 500)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

# Llamar a la función cambiar_escena() cuando se presione la tecla "space"
                def activar_cambio_escena():
                        turtle.onkey(cambiar_escena, "space") 

                turtle.listen()

# Llamar a activar_cambio_escena() para configurar la tecla "space"
                activar_cambio_escena()
                turtle.mainloop()









turtle.penup()
turtle.goto(turtle.xcor(), turtle.ycor() - 500)
turtle.write("Si quiere empezar el cuento presione espacio", font=("Arial", 12))
turtle.goto(turtle.xcor(), turtle.ycor() - 20)

# Llamar a la función cambiar_escena() cuando se presione la tecla "space"
def activar_cambio_escena_inicio():
    turtle.onkey(cambiar_escena_inicio, "space") 

turtle.listen()

# Llamar a activar_cambio_escena() para configurar la tecla "space"
activar_cambio_escena_inicio()
turtle.mainloop()


turtle.done()
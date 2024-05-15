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
        escena= int(turtle.textinput("Coloque la escena a la que quiere trasladarse","5 escenas disponibles, 6 salir"))
        match (escena):
            case 1:
                turtle.pendown()
                turtle.clear()
                turtle.color("black")
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 1: El Comienzo", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("En un bosque muy lejano llamado Bosque Encantado, vivía una ardilla traviesa llama-", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("da Cuki. Cuki era conocida por su curiosidad y su amor por las aventuras. Un día, ", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("mientras saltaba de rama en rama, encontró un mapa antiguo entre las hojas secas.", font=("Arial", 12))  
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)

                def dibujar_circulo(t, radio, color):
                    t.color(color)
                    t.begin_fill()
                    t.circle(radio)
                    t.end_fill()
                def dibujar_rectangulo(t, ancho, altura, color):
                    t.color(color)
                    t.begin_fill()
                    for _ in range(2):
                        t.forward(ancho)
                        t.left(90)
                        t.forward(altura)
                        t.left(90)
                    t.end_fill()

                def dibujar_ardilla(t, color_ardilla):
                    # Cuerpo
                    t.penup()
                    t.goto(-30, -100)
                    t.pendown()
                    dibujar_rectangulo(t, 60, 90, color_ardilla)

                    # Cabeza
                    t.penup()
                    t.goto(-20, -10)
                    t.pendown()
                    dibujar_circulo(t, 30, color_ardilla)

                    # Ojos
                    t.penup()
                    t.goto(-20, 20)
                    t.pendown()
                    dibujar_circulo(t, 5, "black")
                    t.penup()
                    t.goto(-5, 20)
                    t.pendown()
                    dibujar_circulo(t, 5, "black")

                    # Cola
                    t.penup()
                    t.goto(-50, -90)  
                    t.pendown()
                    t.color("black")
                    t.begin_fill()
                    t.left(135)
                    t.forward(80)
                    t.right(90)
                    t.forward(20)
                    t.right(90)
                    t.forward(80)
                    t.right(135)
                    t.end_fill()

                def dibujar_nube(t, x, y):
                    t.penup()
                    t.goto(x, y)
                    t.pendown()
                    dibujar_circulo(t, 20, "white")
                    t.penup()
                    t.goto(x + 30, y)
                    t.pendown()
                    dibujar_circulo(t, 20, "white")
                    t.penup()
                    t.goto(x + 15, y + 15)
                    t.pendown()
                    dibujar_circulo(t, 30, "white")

                def dibujar_arroyo(t):
                    # Cuerpo del arroyo
                    t.penup()
                    t.goto(-300, -200)
                    t.pendown()
                    t.color("blue")
                    t.begin_fill()
                    t.goto(300, -200)
                    t.goto(300, -250)
                    t.goto(-300, -250)
                    t.goto(-300, -200)
                    t.end_fill()

                    # Olas del arroyo
                    for _ in range(6):
                        t.penup()
                        t.goto(-280 + _ * 100, -220)
                        t.pendown()
                        t.goto(-260 + _ * 100, -210)
                        t.goto(-240 + _ * 100, -220)
                        t.goto(-220 + _ * 100, -210)

                def dibujar_cueva(t):
                    t.penup()
                    t.goto(100, -300)
                    t.setheading(90) 
                    t.pendown()

                    t.color("gray")
                    t.begin_fill()
                    t.circle(100, -270)  
                    t.end_fill()

                    t.penup()
                    t.goto(10, -300)
                    t.pendown()
                    t.color("black")
                    t.begin_fill()
                    t.circle(150)
                    t.end_fill()

                def dibujar_grama(t):
                    t.penup()
                    t.goto(-400, -250)
                    t.pendown()
                    t.color("green")
                    t.begin_fill()
                    for _ in range(2):
                        t.forward(800)
                        t.left(90)
                        t.forward(100)
                        t.left(90)
                    t.end_fill()

                def main():
                    ventana = turtle.Screen()
                    ventana.bgcolor("skyblue")

                    t = turtle.Turtle()
                    t.speed(200)

                    # Dibujar escena
                    dibujar_grama(t)
                    dibujar_ardilla(t, "brown")
                    dibujar_nube(t, -100, 150)
                    dibujar_nube(t, 150, 180)
                    dibujar_arroyo(t)
                    dibujar_cueva(t)

                    ventana.mainloop()

                if __name__ == "__main__":
                    main()
                    
                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

            case 3:
                turtle.pendown()
                turtle.clear()
                turtle.color("black")
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 3: El Desafío de la Cueva", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("Dentro de la cueva, Cuki se encontró con un guardián sorpresa: un búho sabio llamado", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("Don Hoot. Para obtener el tesoro, Don Hoot le propuso a Cuki resolver un acertijo.", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("Cuki, con su ingenio, respondió correctamente y ganó la admiración del búho.", font=("Arial", 12))  
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

            case 2:
                turtle.pendown()
                turtle.clear()
                turtle.color("black")
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 2: La búsqueda del tesoro", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("El mapa mostraba el camino hacia un tesoro escondido. Con gran emoción, Cuki ", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write(" decidió seguir el mapa. Atravesó arroyos cristalinos y pasó por campos de", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("flores, hasta llegar a una cueva misteriosa donde, según el mapa, estaba el tesoro.", font=("Arial", 12))  
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

            case 4:
                turtle.pendown()
                turtle.clear()
                turtle.color("black")
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 4: El tesoro descubierto", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("Con el acertijo resuelto, Don Hoot le mostró a Cuki el tesoro: una caja llena de gemas", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("brillantes y una corona de flores. Cuki estaba fascinada por la belleza del tesoro", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("y agradeció al búho con un abrazo de amistad.", font=("Arial", 12))  
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")
               
            case 5:
                turtle.pendown()
                turtle.clear()
                turtle.color("black")
                turtle.teleport(-300,250)
                for x in range(0, 2):
                    turtle.forward(50)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)
                turtle.penup()
                turtle.forward(50)  
                turtle.left(90)
                turtle.forward(50)  
                turtle.write("Titulo escena 5: El regreso a casa", font=("Arial", 16, "bold"))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport(300,-250)
                for x in range(0, 2):
                    turtle.forward(-600)
                    turtle.left(90)
                    for x in range (2,3):
                        turtle.forward(100)
                        turtle.left(90)
                turtle.penup()
                turtle.forward(-590)  
                turtle.left(-90)
                turtle.forward(-65)  
                turtle.write("Llena de alegría y con el tesoro en sus patitas, Cuki regresó al Bosque Encantado. Sus", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write("amigos animales la recibieron con entusiasmo y todos celebraron con una fiesta bajo", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)  
                turtle.write(" la luz de la luna. Desde entonces, Cuki aprendió que las aventuras más valiosas son", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)   
                turtle.write("las compartidas con amigos                                     FIN", font=("Arial", 12))
                turtle.hideturtle()

                turtle.pendown()
                turtle.teleport (-300, 200)
                for x in range(0, 2):
                    turtle.forward(350)
                    turtle.left(-90)
                    for x in range (2,3):
                        turtle.forward(-600)
                        turtle.left(-90)

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")

                turtle.penup()
                turtle.goto(turtle.xcor(), turtle.ycor() - 475)
                turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
                turtle.goto(turtle.xcor(), turtle.ycor() - 20)

                def activar_cambio_escena1():
                    turtle.onkey(cambiar_escena, "space") 

                turtle.listen()
                activar_cambio_escena1()
                turtle.mainloop()
                cambiar_escena()

                def cambiar_escena():
                    turtle.write("", align="center", font=("Arial", 14, "bold"))

                numero_escena = turtle.textinput("AVISOOOOO!", "Desea Cambiar de escena? Presione 6")

                try:
                    numero_escena = int (numero_escena) 
                    print(f"Cambiando a la escena...")  
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número válido.")
            case 6:
                turtle.bye()
        
                





               

# Mover la tortuga a una posición adecuada y mostrar mensaje inicial
turtle.penup()
turtle.goto(turtle.xcor(), turtle.ycor() - 500)
turtle.write("Si quiere cambiar de escena presione la tecla espacio", font=("Arial", 12))
turtle.goto(turtle.xcor(), turtle.ycor() - 20)

# Llamar a la función cambiar_escena() cuando se presione la tecla "space"
def activar_cambio_escena():
    turtle.onkey(cambiar_escena_inicio, "space") 

turtle.listen()

# Llamar a activar_cambio_escena() para configurar la tecla "space"
activar_cambio_escena()
turtle.mainloop()



turtle.done()








    


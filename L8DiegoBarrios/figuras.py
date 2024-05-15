import turtle

import turtle

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



turtle.done()
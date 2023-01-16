import turtle

window = turtle.Screen ()
window.bgcolor ("pink")

def draw_m():
    m = turtle.Turtle ()
    m.shape("turtle")
    m.color ("black")
    m.speed (2)
    m.left(270)
    m.backward (100)
    m.left(45)
    m.forward (50)
    m.left(90)
    m.forward (50)
    m.left(45)
    m.backward (100)

draw_m ()

def draw_c():
    c = turtle.Turtle ()
    c.setposition (200.00,0.00)
    c.shape("turtle")
    c.color ("black")
    c.speed (2)
    c.backward (75)
    c.left(90)
    c.forward (100)
    c.right(90)
    c.forward (75)
    

draw_c ()


window.exitonclick ()

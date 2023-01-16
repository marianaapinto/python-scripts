import turtle

window = turtle.Screen ()
window.bgcolor ("pink")

def draw_mc():
    mc = turtle.Turtle ()
    mc.shape("turtle")
    mc.color ("black")
    mc.speed (2)
    mc.left(270)
    mc.backward (100)
    mc.left(45)
    mc.forward (50)
    mc.left(90)
    mc.forward (50)
    mc.left(45)
    mc.backward (100)
    mc.up ()
    mc.setposition (200.00,0.00)
    mc.down ()
    mc.left(90)
    mc.forward (75)
    mc.right(90)
    mc.forward (100)
    mc.right(90)
    mc.forward (75)

draw_mc ()


window.exitonclick ()

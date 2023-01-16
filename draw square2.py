import turtle

def draw_square ():
    window = turtle.Screen ()
    window.bgcolor ("pink")

    mari = turtle.Turtle ()
    mari.shape ("turtle")
    mari.color ("white")
    mari.speed (2)
    mari. forward (100)
    mari.right (90)
    mari. forward (100)
    mari.right (90)
    mari. forward (100)
    mari.right (90)
    mari. forward (100)
    mari.right (90)
    
    window.exitonclick ()

draw_square ()

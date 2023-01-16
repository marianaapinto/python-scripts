import turtle

def draw_square ():
    window = turtle.Screen ()
    window.bgcolor ("red")

    brad = turtle.Turtle ()
    brad.shape("turtle")
    brad.color ("yellow")

    total_sides = 4
    side_count = 0
    while (side_count < total_sides): 
        brad.forward (100)
        brad.right (90)
        side_count = side_count + 1
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color ("blue")
    angie.circle (100)

    mari = turtle.Turtle()
    mari.shape("arrow")
    mari.color ("green")
    mari.forward (100)
    mari.right (135)
    mari.forward (100)
    mari.right (135)
    mari.forward (100)
        
    
    window.exitonclick ()

draw_square ()

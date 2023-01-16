import turtle

def draw_losangle (some_turtle):
    for i in range (0,2):
        some_turtle.forward(100)
        some_turtle.right(35)
        some_turtle.forward(100)
        some_turtle.right(145)
            
def draw_flower():
    window = turtle.Screen ()
    window.bgcolor ("white")
    flower = turtle.Turtle ()
    flower.shape("turtle")
    flower.color ("black")
    flower.fillcolor ("yellow")
    flower.speed (500)
    for i in range(1,37):
        draw_losangle (flower)
        flower.right (10)
    flower.right (90)
    flower.forward (450)
    flower.up ()
    flower.setposition (0.00,-200.00)
    flower.down ()
    flower.right (40)
    draw_losangle (flower)
    window.exitonclick ()

draw_flower ()

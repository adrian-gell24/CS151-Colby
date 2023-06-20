import turtle
window = turtle.getscreen()
tom = turtle.Turtle()

def draw_hexagon():
    
    for i in range (0,6):
        tom.forward(100)
        tom.left(60)

draw_hexagon()
turtle.exitonclick()
import turtle

screen = turtle.Screen()
screen.bgcolor("black")

tree = turtle.Turtle()
tree.color("green")

tree.left(90)
tree.penup()
tree.goto(0, -250)
tree.pendown()

def branch(length):
    if length < 10:
        return

    tree.forward(length)

    tree.left(30)
    branch(length * 0.7)

    tree.right(60)
    branch(length * 0.7)

    tree.left(30)

    tree.backward(length)



branch(100)

turtle.done()
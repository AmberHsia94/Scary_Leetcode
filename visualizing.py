import turtle

def drawSpiral(myTurtle, lineLen):
    # given a length
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)

# draw a fractal tree
# a fractal is something that looks the same at all different levels of magnification.
def fractal_tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        fractal_tree(branchLen - 15, t)
        t.left(40)
        fractal_tree(branchLen - 15, t)
        t.right(20)
        t.backward(branchLen)

# def sierpinski_triangle(, t)


if __name__ == '__main__':
    myTurtle = turtle.Turtle()  # create a turtle
    myWin = turtle.Screen()  # creates a window for itself to draw in

    # drawSpiral(myTurtle, 100)
    # myWin.exitonclick()

    # myTurtle.left(90)
    # myTurtle.up()
    # myTurtle.backward(100)
    # myTurtle.down()
    # myTurtle.color("green")
    # fractal_tree(75, myTurtle)
    # myWin.exitonclick()
    #  method of the window that puts the turtle into a wait mode
    # until you click inside the window, after which the program cleans up and exits.


    myTurtle.right(60)
    myTurtle.forward(200)
    myTurtle.right(120)
    myTurtle.forward(200)
    myTurtle.right(120)
    myTurtle.forward(200)


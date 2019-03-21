import turtle
FORWARDSIZE = 10
ANGLE = 90


def goTurtleStep(anyTurtle, commandChar):
    """
    a function called goTurtleStep that takes two parameters:
    a turtle , a command character
    makes the turtle execute the command character
    if the command character isn't implemented, then don't do anything.
    """
    if commandChar == "F":
        anyTurtle.forward(FORWARDSIZE)
    elif commandChar == "-":
        anyTurtle.right(ANGLE)
    elif commandChar == "+":
        anyTurtle.left(ANGLE)
    else:
        pass

    return

def goTurtleGo(someTurtle, commandStr):
    """

    :param someTurtle:
    :param commandStr:
    iterates over the characters in the string and performs the goTurtleStep function on them
    :return: nothing
    """
    for char in commandStr:
        goTurtleStep(someTurtle, char)

    return

#Sets up screen
turtle.setup(400, 400)
wn = turtle.Screen()
wn.bgcolor("blue")


hannah = turtle.Turtle()
hannah.pendown()
goTurtleGo(hannah, "FF+F-FF++F")

wn.exitonclick()


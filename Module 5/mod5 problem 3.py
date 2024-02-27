import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()
length=int(input("how long of each sides"))
sides=int(input("what is the number of the sides"))
linecolor=input("what is the linecolor")
fillcolor=input("what is the fill color")
alex.color(linecolor)
alex.fillcolor(fillcolor)
alex.begin_fill()
for i in range(sides):      # repeat four times
    alex.forward(length)
    alex.left(360/sides)
alex.end_fill()
wn.exitonclick()


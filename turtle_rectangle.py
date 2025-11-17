import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightgray")
screen.title("Turtle Combined Shapes")

# Create the turtle
shape_turtle = turtle.Turtle()
shape_turtle.speed(5)

# Draw a rectangle
shape_turtle.color("blue")
for x in range(2):
    shape_turtle.forward(200)
    shape_turtle.left(90)
    shape_turtle.forward(100)
    shape_turtle.left(90)

# Move to a new position
shape_turtle.penup()
shape_turtle.goto(-50, -150)
shape_turtle.pendown()

# Draw a circle
shape_turtle.color("red")
shape_turtle.circle(75)

# Hide the turtle and display the result
shape_turtle.hideturtle()
screen.mainloop()

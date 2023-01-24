import turtle

t = turtle.Turtle()
t.up()

BOTTOM_LEFT = (-410, -330)
BOTTOM_RIGHT = (365, -330)
DISTANCE = 85

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.bgpic("soil.png")

t.width(10)
t.pencolor("blue")

t.goto(BOTTOM_LEFT)
t.left(60)
clay = int(input("enter percent clay: "))
t.forward(DISTANCE * (clay / 10))
t.right(120)
t.down()
t.forward(500)

t.up()
t.goto(BOTTOM_LEFT)
t.left(60)
sand = int(input("enter percent sand: "))
t.forward(DISTANCE * ((100 - sand) / 10))
t.down()
t.left(60)
t.forward(500)


t.up()
t.goto(BOTTOM_RIGHT)
t.left(60)
silt = int(input("enter percent silt: "))
t.forward(DISTANCE * ((100 - silt) / 10))
t.down()
t.left(120)
t.forward(500)


screen.mainloop()

import turtle as turtle_module
import random
turtle_module.screensize(3000,3000)
tur = turtle_module.Turtle()
turtle_module.colormode(255)
tur.speed("fastest")
tur.penup()
tur.hideturtle()
spacing = 15
r = 2 * spacing
number_of_circles = 2*10*spacing
color_list = [(244, 242, 237), (228, 234, 241), (245, 237, 241), (235, 243, 238), (214, 157, 85), (33, 105, 151), (238, 215, 94), (153, 75, 52), (125, 168, 199), (209, 134, 163), (156, 60, 81), (22, 39, 54), (212, 85, 61), (176, 162, 47), (200, 85, 119), (135, 184, 150), (56, 119, 90), (240, 213, 4), (25, 46, 37), (228, 167, 186), (64, 46, 34), (87, 157, 100), (9, 99, 75), (34, 166, 189), (40, 60, 102), (228, 175, 166), (179, 189, 213), (95, 126, 173), (68, 34, 44), (105, 42, 60), (170, 205, 179), (113, 43, 37), (156, 206, 217), (78, 69, 35), (3, 90, 115)]
def R_circle():
    tur.dot(r-1, random.choice(color_list))
    for i in range(0, number_of_circles, spacing):
        tur.setx(r + 2 * i)
        tur.setheading(90)
        angle = 360 / (6 * (i/spacing+1) )
        for _ in range(int(6*(i/spacing+1))):
            tur.dot(r-1,random.choice(color_list))
            t = tur.circle(r + 2*i, angle)
R_circle()
def save():
    ts = turtle_module.getscreen()
    ts.getcanvas().postscript(file="Square.png")
turtle_module.onkeypress(save(), key="q")

screen = turtle_module.Screen()
screen.exitonclick()
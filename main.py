import turtle
from turtle import Screen, Turtle

screen = Screen()

screen.title("Australia State Game")
screen.register_shape('au_statues.gif')
turtle.shape('au_statues.gif')

screen.setup(width=800, height=800)

def get_location_coordinates(x, y):
    print(x, y)

turtle.onscreenclick(get_location_coordinates)
turtle.mainloop()

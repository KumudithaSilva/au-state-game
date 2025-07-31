import pandas
import csv
import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.title("Australia State Game")
screen.register_shape('au_map.gif')
turtle.shape('au_map.gif')
screen.setup(width=810, height=810)

data = pandas.read_csv("au_city.csv")
data_length = len(data)
all_states = data.state.to_list()
guessed_status = []

def get_location_coordinates(x, y):
    au_state = screen.textinput(title="Save the City", prompt="Save the city's name")
    with open("au_city.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([au_state, x, y])

def set_location_coordinates(x, y):
    pass

while len(guessed_status) < data_length:
    answer_state = screen.textinput(title=f"{len(guessed_status)}/{data_length} Status Correct", prompt="What's another city's name?").title()
    if answer_state in all_states:
        guessed_status.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        x = state_data["x"].item()
        y = state_data["y"].item()
        t.goto(x, y)
        t.dot(5, "red")
        t.write(answer_state, font=("Impact", 15, "normal"))


# turtle.onscreenclick(set_location_coordinates)
screen.exitonclick()
turtle.mainloop()

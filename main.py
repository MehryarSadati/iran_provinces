import turtle
import pandas

screen = turtle.Screen()
screen.title("Iran states game")
image = "iran_map.gif"
screen.addshape(image)
screen.setup(width= 1200, height= 1071)
turtle.shape(image)

t = turtle.Turtle()
t.penup()
t.hideturtle()

persian_data = pandas.read_csv("ostans.csv")
# x_axis = data.x.to_list()
# y_axis = data.y.to_list()

english_data = pandas.read_csv("english_ostans.csv")
# english_ostans = english_data.ostan.to_list()

language = screen.textinput(title= "language", prompt="would you rather english names or persian names?(english/persian)")
if language == "english":
    data = english_data
else:
    data = persian_data

ostans = data.ostan.to_list()

right_answers = 0
is_game_on = True
while is_game_on:
    answer = screen.textinput(title= f"{right_answers}/31 ostans correct", prompt= "name a ostan in iran:").lower()
    if answer == "exit":
        is_game_on = False

    for ostan in ostans:
        if answer == ostan.lower():
            right_answers += 1
            location = data[data.ostan == ostan]
            t.goto(int(location.x), int(location.y))
            t.write(ostan)
            ostans.remove(ostan)
    if right_answers == 31:
        t.goto(0,0)
        t.write("CONGRATULATIONS",align= "center", font=("Arial", 50,"bold"))
        is_game_on = False

un_guessed_states = pandas.DataFrame(ostans)
un_guessed_states.to_csv("learn_the_ostans_you_missed.csv")

screen.exitonclick()
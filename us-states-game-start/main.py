import turtle
import pandas

clicker = turtle.Turtle()
timmy = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=1.0, height=1.0)
image = "blank_states_img.gif"
screen.addshape(image)
timmy.shape(image)

#open and make cvs list usable
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(all_states) > 0:
    guess = screen.textinput(title=f"  {50 - len(all_states)}/50 States Correct", prompt="What's another state name?").title()
    if guess in all_states:
        all_states.remove(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    elif guess == "Exit":
        missed_states = pandas.DataFrame(all_states)
        missed_states.to_csv("missed states.csv")
        break


screen.exitonclick()
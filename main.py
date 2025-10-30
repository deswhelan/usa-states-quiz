import turtle

import pandas

ALIGN = "center"
BG_IMAGE_PATH = "blank_states_img.gif"
FONT = ("Courier", 6, "bold")
GAME_TITLE = "Name the States"
STATE_DATA_PATH = "50_states.csv"

screen = turtle.Screen()
screen.title(GAME_TITLE)
screen.addshape(BG_IMAGE_PATH)

turtle.shape(BG_IMAGE_PATH)

state_data = pandas.read_csv(STATE_DATA_PATH)

user_score = 0
correct_guesses = []

def display_state_label(state):
    label = turtle.Turtle()
    label.penup()
    label.hideturtle()
    label.goto((state.x.item(), state.y.item()))
    label.write(state.name.item(), align=ALIGN, font=FONT)

print(state_data)

while user_score < 50:
    user_guess = screen.textinput(title=f"Score: {user_score}/50", prompt="Enter your guess: ").lower()

    for state_name in state_data.name:
        if state_name.lower() == user_guess and user_guess not in correct_guesses:
            user_score += 1
            correct_guesses.append(user_guess)
            display_state_label(state_data[state_data.name == state_name])

print("Congratulations, YOU WIN!")

turtle.mainloop()
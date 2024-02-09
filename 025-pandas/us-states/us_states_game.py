import turtle
import pandas

# def get_mouse_click_coords(x, y):
#     print(x, y)

# For finding the relevant coords for placing name
# - was used to determine x, y coords in the csv file
# turtle.onscreenclick(get_mouse_click_coords)

MAP_IMAGE = "./blank_states_img.gif"
STATES_DATA = "./50_states.csv"
MISSED_STATES = "./missed_states.csv"
LABEL_FONT = ("Arial", 7, "bold")


def create_state_label(state: str, x: int, y: int):
    coords = (x, y)
    label = turtle.Turtle()
    label.hideturtle()
    label.penup()
    label.goto(coords)
    label.write(state, font=LABEL_FONT)


screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(MAP_IMAGE)
turtle.shape(MAP_IMAGE)

states_df = pandas.read_csv(STATES_DATA)
guessed_states = []

while len(guessed_states) < 50:
    title = f"You've correctly guessed {len(guessed_states)}/50"
    if len(guessed_states) < 1:
        title = "Guess the State"

    # Convert answer to title case for matching DF state values
    answer_state = screen.textinput(
        title=title,
        prompt="Give me the name of another U.S. State"
    ).title()

    if answer_state == "Exit":
        # Use list comprehension to find 'unguessed' states
        if len(guessed_states) < 50:
            missed_states = [state for state in states_df.state.to_list() if state not in guessed_states]
            missed_df = pandas.DataFrame(missed_states)
            missed_df.columns = ["state"]
            missed_df.to_csv(MISSED_STATES, index=False)
        break

    state_df = states_df[states_df.state == answer_state]
    if not state_df.empty:
        guessed_states.append(answer_state)
        # item() returns first element in Series
        #  - since state_df is single row DF, each column series is a single item
        create_state_label(state_df.state.item(), int(state_df.x.item()), int(state_df.y.item()))

# Alternative to screen.exitonclick() for keeping screen open
# turtle.mainloop()

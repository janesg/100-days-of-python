import os

PLACE_HOLDER = "[name]"

# Create the output folder if it doesn't exist
if not os.path.exists("./Output"):
    os.makedirs("./Output")

with open("./Input/Letters/birthday_invite_template.txt") as template:
    lines = template.readlines()

with open("./Input/Names/invited_names.txt") as name_file:
    # Remove the trailing '\n' from each name
    names = list(map(lambda nm: nm.rstrip("\n"), name_file.readlines()))

    for name in names:
        with open(f"./Output/birthday_invite_for_{name}.txt", "w") as invite:
            for line in lines:
                invite.write(line.replace(PLACE_HOLDER, name))

import os
import platform
import random
from art import higher_lower, vs
from game_data import data


def format_person(person: dict) -> str:
    return f"{person['name']}, a {person['description']}, from {person['country']}"


game_over = False
score = 0
person_a = data[random.randint(0, len(data) - 1)]

while not game_over:
    os.system("cls" if platform.system() == 'Windows' else "clear")

    print(higher_lower)
    if score > 0:
        print(f"You are correct ... current score is {score}")

    print(f"Compare A: {format_person(person_a)}")
    print(vs)
    person_b = data[random.randint(0, len(data) - 1)]
    print(f"Compare B: {format_person(person_b)}")

    guess_a = input("Who has more Instagram followers? Is it 'A' or 'B' : ").lower().startswith('a')

    if guess_a:
        if person_a['follower_count'] > person_b['follower_count']:
            score += 1
            person_a = person_b
        else:
            game_over = True
    else:
        if person_b['follower_count'] > person_a['follower_count']:
            score += 1
            person_a = person_b
        else:
            game_over = True

print(f"Sorry, that was wrong ... your final score was {score}")

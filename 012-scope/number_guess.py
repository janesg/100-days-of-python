import random

logo = """
       ______                        __  __            _   __                __             
      / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
     / / __/ / / / _ \\/ ___/ ___/  / __/ __ \\/ _ \\   /  |/ / / / / __ `__ \\/ __ \\/ _ \\/ ___/
    / /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
    \\____/\\__,_/\\___/____/____/   \\__/_/ /_/\\___/  /_/ |_/\\__,_/_/ /_/ /_/_.___/\\___/_/     
    """

def the_game():
    print(logo)
    print("I'm thinking of a number in the range of 1 to 100.")
    is_easy = input("Choose a difficulty. Type (e)asy or (h)ard : ").lower().startswith('e')
    attempts_remaining = 10 if is_easy else 5
    the_number = random.randint(1, 100)

    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempt(s) remaining to guess the number")
        guess = int(input("Guess the number : "))

        if guess == the_number:
            print(f"Congratulations, you guessed that the number was {the_number}")
            exit(0)
        else:
            print(f"No, the number is not {guess}... it is {"lower" if guess > the_number else "higher"} than that.")
            attempts_remaining -= 1

    print(f"Unlucky, you didn't manage to guess that the number was {the_number}")

the_game()
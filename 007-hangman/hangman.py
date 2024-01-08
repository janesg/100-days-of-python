# import os
# import platform
import random
from hangman_words import word_list

# clear_cmd = "cls" if platform.system() == "Windows" else "clear"
chosen_word = word_list[random.randint(0, len(word_list) - 1)].lower()
word_frame = [" "] * len(chosen_word)
guesses = []
# It takes 6 goes to draw the hung man's head, body, arms & legs
lives = 6

def print_word_frame():
    print("")
    print("".join(word_frame))
    print(f"{'=' * len(word_frame)}")

def finished():
    if lives == 0:
        print("")
        print("**************************************************************************")
        print(f"*** You lost coz you ran out of lives! The word was: {chosen_word}")
        print("**************************************************************************")
        return True
    elif " " not in word_frame:
        print("")
        print("**************************************************************************")
        print(f"*** You won by correctly guessing the word: {chosen_word}")
        print("**************************************************************************")
        return True
    else:
        return False

print_word_frame()

while not finished():
    guess = input("\nEnter your guess: ").lower()
    # os.system(clear_cmd)

    if guess not in guesses:
        guesses.append(guess)

    if guess in chosen_word:
        for i in range(0, len(chosen_word)):
            if chosen_word[i] == guess:
                word_frame[i] = guess
    else:
        print(f"Wrong... '{guess}' is not in the word. Lose a life!")
        lives -= 1

    print_word_frame()
    print(f"Lives remaining: {lives}")
    print(f"So far, you have guessed: {guesses}")

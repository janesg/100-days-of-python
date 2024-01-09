alphabet = [chr(i) for i in range(97, 123)]


def shifted_alphabet(shift: int) -> list[chr]:
    alpha_shift = []
    for i in range(shift, len(alphabet)):
        alpha_shift.append(alphabet[i])
    for i in range(0, shift):
        alpha_shift.append(alphabet[i])

    return alpha_shift


def encrypt(text: str, shift: int) -> str:
    shifted = shifted_alphabet(shift)

    cipher_text = []
    for letter in text:
        try:
            index = alphabet.index(letter)
            cipher_text.append(shifted[index])
        except ValueError:
            cipher_text.append(letter)

    return "".join(cipher_text)


def decrypt(text: str, shift: int) -> str:
    shifted = shifted_alphabet(shift)

    clear_text = []
    for letter in text:
        try:
            index = shifted.index(letter)
            clear_text.append(alphabet[index])
        except ValueError:
            clear_text.append(letter)

    return "".join(clear_text)


while True:
    action = input(f"What action do you want to perform ? (e)ncrypt, (d)ecrypt or return to exit: ").lower()

    if not action:
        exit(0)
    elif not action.startswith("e") and not action.startswith("d"):
        print(f"An action of '{action}' is invalid")
        exit(1)

    shift = int(input(f"How many characters do you want to shift by ? : "))

    if shift < 0 or shift > 25:
        print(f"A shift of {shift} character(s) is invalid")
        exit(1)

    text = input("Type the text to be actioned : ").lower()

    if action.startswith("e"):
        print(f"Encrypted text : {encrypt(text, shift)}")
    else:
        print(f"Decrypted text : {decrypt(text, shift)}")

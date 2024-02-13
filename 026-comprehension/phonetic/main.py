import pandas

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index,row) in phonetic_df.iterrows()}
print(phonetic_dict)

# Create a list of the phonetic code words from a word that the user inputs.
exit_loop = False
while not exit_loop:
    word = input("Please enter the word you want to spell phonetically: ").upper()

    try:
        print([phonetic_dict[letter] for letter in word])
    except KeyError:
        print("Sorry, only alphabetic characters please...try again")
    else:
        exit_loop = True
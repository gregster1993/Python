import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

game_is_on = True

while game_is_on:
    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)
    choice = input("Do you want top continue? (Yes or No) ").lower()
    if choice == "no":
        game_is_on = False
    else:
        pass


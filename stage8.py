import random

words = ["python", "java", "kotlin", "javascript"]
lives = 8
guesses = []
menu_choice = ""

def print_state():
    print()
    print(hidden_word)

def update_hidden_word(guess_letter):
    global hidden_word
    indices = []

    for i in range(0, len(correct_word)):
        if correct_word[i] == guess_letter:
            indices.append(i)

    new_string = ""

    for i in range(0, len(correct_word)):
        if len(indices) != 0:
            if i == indices[0]:
                new_string += guess_letter
                del indices[0]
            else:
                if hidden_word[i] != "-":
                    new_string += hidden_word[i]
                else:
                    new_string += "-"
        else:
            if hidden_word[i] != "-":
                new_string += hidden_word[i]
            else:
                new_string += "-"

    hidden_word = new_string

# Correct word determined
random.seed()
correct_word = words[random.randint(0, 3)]
hidden_word = "-" * len(correct_word)

print("H A N G M A N")

while menu_choice != "exit":
    menu_choice = input("Type \"play\" to play the game, \"exit\" to quit: ")

    if menu_choice == "play":
        while lives >= 1:
            if hidden_word == correct_word:
                print("You guessed the word {}!".format(correct_word))
                print("You survived!\n")
                break

            print_state()

            letter = input("Input a letter: ")

            if letter in set(correct_word) and letter not in hidden_word:
                update_hidden_word(letter)
            else:
                if (letter == "" or "-" in letter) or letter not in hidden_word:
                    if len(letter) != 1:
                        print("You should input a single letter")
                    elif not letter.isalpha() or not letter.islower():
                        print("Please enter a lowercase English letter")
                    else:
                        if letter in guesses:
                            print("You've already guessed this letter")
                        else:
                            print("That letter doesn't appear in the word")
                            lives -= 1
                            guesses.append(letter)
                else:
                    print("You've already guessed this letter")
        else:
            print("You lost!\n")

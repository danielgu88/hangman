import random

words = ["python", "java", "kotlin", "javascript"]
random.seed()
correct_word = words[random.randint(0, 3)]

print("H A N G M A N")
word = input("Guess the word {}{}:".format(correct_word[:3], "-" * (len(correct_word) - 3)))

if word == correct_word:
    print("You survived!")
else:
    print("You lost!")

import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6
word_length = len(chosen_word)

print(logo)

placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    guess = input("Guess a letter\n").lower()
    display = ""
    for letter in chosen_word:
        if (letter == guess):
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])
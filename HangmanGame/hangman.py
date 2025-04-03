import random

display = 0

word_list = ["avocado", "football", "basketball", "gaming", "witcher", "apple", "computer"]
chosen_word = list(random.choice(word_list))

blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

def quessing_game():
    index = 0
    global display
    correct_quess = False
    for letter in chosen_word:
        if quess.lower() == chosen_word[index]:
            blank_list[index] = quess.lower()
            correct_quess = True
        index += 1
    if correct_quess == False:
        print(f"There was no {quess} in our secret word.")
        display += 1

    

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

print(HANGMANPICS[display])
print(chosen_word)
quess = input("Welcome to Hangman Game! \nMake a quess: ")
quessing_game()
print(HANGMANPICS[display])
print(''.join(blank_list))

while display < 6:
    if blank_list == chosen_word:
        print("You win!")
        break
    quess = input("Make a quess: ")
    quessing_game()
    print(HANGMANPICS[display])
    print(''.join(blank_list))

if display == 6:
    print("GAME OVER!")
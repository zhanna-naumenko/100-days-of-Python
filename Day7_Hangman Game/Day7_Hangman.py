import random
import Day7_Hangman_words
import Day7_Hangman_ascii

# printing welcoming
print("Hello! Wellcome to the Hangman game!")
print(Day7_Hangman_ascii.logo)

# choosing the random word from the list
random_word = random.choice(Day7_Hangman_words.words)

# making a list from the letters of the random word
list_of_letters = list(random_word)

# making the list of "_" blank list to show the player how many letters are in the word
blank_list = list("_" * len(random_word))
# printing the blanks to show the user the length of the word
print("".join(blank_list))
# counting the number of guesses
numb_of_guess = 0
# track the number of mistakes
numb_of_mistakes = len(Day7_Hangman_ascii.hangman_steps)

# make a while loop to check if the player guessed the whole word, or if the number of mistakes is out of the limit
while numb_of_guess < numb_of_mistakes and "_" in blank_list:
    # ask the user to choose the letter. All letters will be in lowercase
    user_choice = input("Guess a letter: ").lower()
    found = False
    # check guessed letter
    for index in range(len(list_of_letters)):
        if list_of_letters[index] == user_choice:
            blank_list[index] = user_choice
            found = True
    # if guess is wrong, increase mistakes and show hangman
    if not found:
        print(Day7_Hangman_ascii.hangman_steps[numb_of_guess])
        numb_of_guess += 1
    print("".join(blank_list))

# final result
if "_" in blank_list:
    print(f"You loose!\n The word was: {random_word}")
else:
    print("You WIN!")

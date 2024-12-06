# Problem Set 2, hangman.py
# To run: python3 hangman.py

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # Check if the secret_word is empty
    if len(secret_word) == 0:
        return True

    # Check if the letters guessed are empty
    if len(letters_guessed) == 0:
        return False

    # Check if the letters guessed are in the secret word
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # Defining the variable progress
    progress = ""

    # Check if the secret_word is empty
    if len(secret_word) == 0:
        progress = " "
        return progress

    # Check if the letters guessed are empty
    if len(letters_guessed) == 0:
        for i in range(len(secret_word)):
            progress = progress + "*"
        return progress

    # Check if the letters guessed are in the secret word in order to show them
    for letter in secret_word:
        if letter in letters_guessed:
            progress = progress + letter
        else:
            progress = progress + "*"
    return progress

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # Set list of all letters and variable to available letters
    alphabet = string.ascii_lowercase
    available_letters = ""

    # Check if the letters guessed are empty
    if len(letters_guessed) == 0:
        available_letters = alphabet
        return available_letters

    # Check if the letters guessed are part of the options available
    for letter in alphabet:
        if letter not in letters_guessed:
            available_letters += letter # Add the letter if it hasn't been guessed
    return available_letters


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    guesses_remaining = 10
    alphabet = string.ascii_lowercase
    vowels = [a, e, i, o, u]
    letters_guessed = []

    print("Welcome to Hangman!")
    # Display how many letters the secret words contains
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while guesses <= 0:
        print("--------------")
        print(f"You have {guesses_remaining} guesses left.") # Guesses remaining
        print(f"Available letters: {get_available_letters(letters_guessed)}") # Letters that have not yet been guessed
        guess = input("Please guess a letter: ") # Ask the user to guess a letter
        guess = lower(guess)
        
        # Use of help
        if guess == "!":
            # The user needs 3 guesses remaining to ask for help
            with_help = True
            if guesses_remaining > 3:
                print("You don't have enough guesses remaining to ask for help.")
            else:
                guesses_remaining = guesses_remaining - 3
                # Help function

        # Filter the answer of the user
        if len(guess) != 1:
            print("That is not a valid letter. Please input a letter from the alphabet.")
        else if guess not in alphabet:
            print("That is not a valid letter. Please input a letter from the alphabet.")
        else if guess in letters_guessed:
            print(f"Oops! You already guessed that letter: {get_word_progress(letters_guessed)}")
        else:
            if guess not in secret_word:
                if guess in vowels:
                    guesses_remaining = guesses_remaining - 2 # Update guesses based on election (vowel)
                else:
                    guesses_remaining = guesses_remaining - 1 # Update guesses based on election (consonant)

                print(f"Oops! That letter is not in my word: {get_word_progress(letters_guessed)}")
            else: 
                letters_guessed.append(guess)
                print(f"Good guess: {get_word_progress(letters_guessed)}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass


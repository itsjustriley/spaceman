import random
words_list = []
def load_word():
    global words_list
    f = open('words.txt', 'r')
    words_list = f.read().split()
    f.close()
    secret_word = random.choice(words_list)
    return secret_word

def startup(secret_word): 
    print("Let's play Sinister Spaceman!") 
    print("Guess the secret word:")
    hidden_word = "_" * len(secret_word)
    print(hidden_word)

def guess(guessed_letters):
    valid = False
    while valid == False:
        guess = input("Guess a letter > ").lower()
        if guess.isalpha() != True or len(guess) > 1:
            print("Invalid entry. Please enter a single letter.")
        elif guess in guessed_letters:
            print("That letter has already been guessed. \nPlease enter a new letter.")
        else:
            valid = True
    return guess

def is_guess_in_word(guess, secret_word, guesses_left):
    # check if guessed letter in secret word
    # args: guess (str): 1 letter user guessed this round, secret_word
    # return: True if guess in in secret_word, else False

    #TODO: check if the letter guess is in the secret word
    if guess not in secret_word:
        print(f"{guess} is NOT in the secret word.")
        guesses_left -= 1
    else:
        print(f"{guess} IS in the secret word!")
    return guesses_left

def is_word_guessed(secret_word, letters_guessed):
    # checks if all letters of secret word have been guessed
    # args: secret_word (string): the random word user needs to guess, letters_guess (list of str): list of guessed letters so far
    # returns: bool: True if all letters are guessed, else false
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for letter in secret_word:
        if letter not in letters_guessed: 
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    # get string showing guessed letters in place for secret word, and underscores for unguessed
    # args: secret_word (string), letters_guessed
    # return: string of letters (guessed) and underscores (unguessed)

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    results = ''
    for letter in secret_word: 
        if letter not in letters_guessed:
            results += "_"
        else:
            results += letter
    return results

def play_again ():
    choice = ''
    while choice != 'y' and choice != 'n':
        choice = input("Would you like to play again? (y/n) \n > ").lower()
        if choice != 'y' and choice != 'n':
            print("Invalid choice. Please enter 'y', or 'n'")
    
    if choice == 'y':
        return True
    else:
        print("Thank you for playing! Goodbye!")
        return False

def spaceman_art (secret_word, guesses_left):
    asciiList = [
    "            _..._", 
    "          .'     '.      _", 
    "         /    .-\"\"-\   _/ \\", 
    "       .-|   /:.   |  |   |", 
    "       |  \  |:.   /.-'-./", 
    "       | .-'-;:__.'    =/", 
    "       .'=  *=|NASA _.='", 
    "      /   _.  |    ;", 
    "     ;-.-'|    \   |", 
    "    /   | \    _\  _\\", 
    "    \\__/'._;.  ==' ==\\", 
    "             \    \   |", 
    "             /    /   /", 
    "             /-._/-._/", 
    "      jgs    \   `\  \\", 
    "              `-._/._/", 
    ]
        
    taken = len(secret_word) - guesses_left
    percent_done = (taken / len(secret_word))
    lines_to_draw = round(percent_done * len(asciiList))
    
    for i in range(lines_to_draw):
        print(asciiList[i])

def word_match(word, secret_word, guessed_letters):
    if len(word) != len(secret_word):
        return False
    for i in range(len(word)):
        if word[i] in guessed_letters and word[i] != secret_word[i]:
            return False
        elif secret_word[i] in guessed_letters and word[i] != secret_word[i]:
            return False
    return True

def sinister_swap(secret_word, guessed_letters):
    global words_list
    possible_words = []
    for word in words_list:
        if (word_match(word, secret_word, guessed_letters)):
            possible_words.append(word)
    if len(possible_words) > 1:
        print('The word has chaged!')
        return random.choice(possible_words)
    else:
        print('The word could not be changed.')
        return secret_word


def spaceman(secret_word):
    # control the game, start in command line
    # args: secret_word
        startup(secret_word)
        alive = True 
        guessed_letters = ""
        guesses_remain = len(secret_word)
        while alive == True:
            user_guess = guess(guessed_letters)
            guesses_remain = is_guess_in_word(user_guess, secret_word, guesses_remain)
            spaceman_art(secret_word, guesses_remain)
            guessed_letters = guessed_letters + user_guess
            if is_word_guessed(secret_word, guessed_letters) == True:
                print("You win!")
                print(f"The word was {secret_word}")
                alive = False
            elif guesses_remain == 0:
                print("You lose.")
                print(print(f"The word was {secret_word}"))
                alive = False
            else:
                print(guessed_letters)
                print(get_guessed_word(secret_word, guessed_letters))
                print(f"You have {guesses_remain} incorrect guesses remaining.")
                secret_word = sinister_swap(secret_word, guessed_letters)

def game():
    play = True
    while play == True:
        secret_word = load_word()
        spaceman(secret_word)
        play = (play_again())
    

#These function calls that will start the game

game()



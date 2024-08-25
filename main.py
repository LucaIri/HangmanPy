import string
import random

def greeting(target):
    name = input("Hello! What is your name?\n")
    print("Greetings {}! Welcome to Hangman!\n".format(name))
    print("Guess this word: ")
    underscore_target = ""
    for i in range(len(target)):
        if target[i] != ' ':
            underscore_target += '_'
        else:
            underscore_target += ' '
    list(underscore_target)
    joined_underscore_target = " ".join(underscore_target)
    print(joined_underscore_target)
    hint_message = "\nHINT: country names ;)\n"
    print(hint_message)
    return joined_underscore_target

def target_word_selection(word_list):
    target_word = random.choice(word_list)
    return target_word

def player_guess(target,unsolved):
    guess = input("Guess a letter!: \n").upper()
    if len(guess)>1:
        print("Only 1 character at a time! Try Again")
        player_guess(target)
    if guess in target:
        
    
    

guess_wrong_limit = 10
target_word_list = ["ARGENTINA", "ANGOLA", "BRAZIL", "BOLIVIA","CANADA", "UNITED STATES", "DOMINICAN REPUBLIC", "RUSSIA", "SPAIN", "FRANCE", "MONGOLIA", "CHINA"]
target_word = target_word_selection(target_word_list)
unsolved_word = greeting(target_word)
while guess_wrong_limit > 0:
    player_guess(target_word, unsolved_word)
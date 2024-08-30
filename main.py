import string
import random

#Opening statement, prompts user for name
def greeting():
    name = input("Hello! What is your name?\n")
    print("Greetings {}! Welcome to Hangman!\n".format(name))
    hint_message = "HINT: country names ;)\n"
    print(hint_message)
    print("Guess this word: ")
    

#prints string of '_' representing the unsolved word,
#  returns the string
def print_blanks(target):    
    underscore_target = ""
    for i in range(len(target)):
        if target[i] != ' ':
            underscore_target += '_'
        else:
            underscore_target += ' '
    
    blank_output = underscore_target_output(underscore_target)
    print(blank_output)
    return underscore_target

#takes in a string, joins it to look more presentable
#  or user, returns string with spaces
def underscore_target_output(target):
    list(target)
    joined_underscore_target = " ".join(target)
    return joined_underscore_target
    

#determines target word, returns target word
def target_word_selection(word_list):
    target_word = random.choice(word_list)
    return target_word

#handles player guesses, if player guess is 
# correct, the associated blanks will be replaced with the
#  guess, returns the unsolved string with blanks
def player_guess(target, unsolved, count):
    right_guess = False
    list_unsolved = list(unsolved)
    guess = input("Guess a letter!: \n").upper()
    if len(guess)>1:
        print("Only 1 character at a time! Try Again")
        player_guess(target)
    if guess in target:
        for i in range(len(unsolved)):
            if target[i] == guess:
                list_unsolved[i] = guess
                right_guess = True
        print("Nice! Keep Going!\n")
    if guess not in target:
        count -= 1
    str_unsolved = "".join(list_unsolved)
    print()
    return str_unsolved
    
    

guess_wrong_limit = 10
target_word_list = ["ARGENTINA", "ANGOLA", "BRAZIL", "BOLIVIA","CANADA", "UNITED STATES", "DOMINICAN REPUBLIC", "RUSSIA", "SPAIN", "FRANCE", "MONGOLIA", "CHINA"]
target_word = target_word_selection(target_word_list)
greeting()
underscore_target_no_space = print_blanks(target_word)
while guess_wrong_limit > 0:
    underscore_target_no_space = player_guess(target_word, underscore_target_no_space, guess_wrong_limit)
    print(underscore_target_output(underscore_target_no_space))
    # if player_guess(target_word, underscore_target_no_space) != True:
    #     guess_wrong_limit -= 1
    #     print("Letter not found! {} mistakes remaining!".format(guess_wrong_limit))

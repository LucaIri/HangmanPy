import string
import random
import re

def greeting():
    name = input("Hello! What is your name?\n")
    print("Greetings {}! Welcome to Hangman!\n".format(name))
    hint_message = "HINT: country names ;)\n"
    print(hint_message)

def target_word_selection(word_list):
    target_word = random.choice(word_list)
    return target_word

def player_guess(target):
    guess = input("Guess a letter!: \n")

guess_wrong_limit = 10
greeting()
target_word_list = ["ARGENTINA", "ANGOLA", "BRAZIL", "BOLIVIA","CANADA", "UNITED STATES", "DOMINICAN REPUBLIC", "RUSSIA", "SPAIN", "FRANCE", "MONGOLIA", "CHINA"]
target_word = target_word_selection(target_word_list)
while guess_wrong_limit < 10:
    player_guess(target_word)
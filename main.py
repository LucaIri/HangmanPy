import string
import random

#Opening statement, prompts user for name
def greeting():
    name = input("Hello! What is your name?\n")
    print("Greetings {}! Welcome to Hangman!\n".format(name))
    hint_message = "HINT: country names ;)\n"
    print(hint_message)
    print("Guess this word: ")
class word:
    def __init__(self, target, blanks, valid):
        self.target = ""
        self.blanks = ""
        self.valid = False

    #determines target word, returns target word
    def target_word_selection(self, word_list):
        target_word = random.choice(word_list)
        self.target =target_word

    

    #prints string of '_' representing the unsolved word,
    #  returns the string
    def print_blanks(self):    
        underscore_target = ""
        for i in range(len(self.target)):
            if self.target[i] != ' ':
                underscore_target += '_'
            else:
                underscore_target += ' '
        list(underscore_target)
        joined_underscore_target = " ".join(underscore_target)
        self.blanks = joined_underscore_target
        print(self.blanks)  


    #handles player guesses, if player guess is 
    # correct, the associated blanks will be replaced with the
    #  guess, returns the unsolved string with blanks
    def player_guess(self):
        temp_blank = self.blanks.split(' ')
        guess = input("Guess a letter!: ").upper()
        if len(guess)>1:
            print("Only 1 character at a time! Try Again")
            self.player_guess()
        if guess == 'q' or 'Q':
            quit()
        if guess in self.target:
            for i in range(len(self.target)):
                if self.target[i] == guess:
                    temp_blank[i] = guess
            print("\nNice! Keep Going!\n")
            self.valid = True
        if guess not in self.target:
            self.valid = False
            print("\nNot in word, try again!\n")
        str_unsolved = " ".join(temp_blank)
        self.blanks = str_unsolved
        print(self.blanks)



    
    
correct = word("","",False)
guess_wrong_limit = 10
target_word_list = ["ARGENTINA", "ANGOLA", "BRAZIL", "BOLIVIA","CANADA", "UNITED STATES", "DOMINICAN REPUBLIC", "RUSSIA", "SPAIN", "FRANCE", "MONGOLIA", "CHINA"]
correct.target_word_selection(target_word_list)
greeting()
correct.print_blanks()
while guess_wrong_limit > 0:
    correct.player_guess()
    if correct.valid == False:
        guess_wrong_limit -=1

#    print(underscore_target_output(underscore_target_no_space))
#    # if player_guess(target_word, underscore_target_no_space) != True:
#    #     guess_wrong_limit -= 1
#    #     print("Letter not found! {} mistakes remaining!".format(guess_wrong_limit))

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import hangman
import os

from english_words import get_english_words_set
web2set = get_english_words_set(['web2'])

def clear():
    os.system("clear")

def pick_random_word(web2set):
    word = random.choice(web2set).upper()
    while len(word) < 7:
        word = random.choice(web2set).upper()
    return word

def print_the_word(correct_guess, word):
    for letter in word:
        if letter in correct_guess:
            print(' {} '.format(letter),end='')
        else:
            print(' _ ', end='')
    
def letter_choice():
    hangman_values = ['O','/','|','\\','|','/','\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    hangman.print_hangman(show_hangman_values)
    letter= input('Enter the letter here:')
    if len(letter) != 1 or not letter.isalpha():
        print('Please enter only single letters')
        letter= input('Enter the letter here:')
    return (letter.upper())

def check_letter(word):
    clear()
    chances= 0
    correct_guess= []
    incorrect_guess= []
    hangman_values = ['O','/','|','\\','|','/','\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while True:
        hangman.print_hangman(show_hangman_values)
        print_the_word(correct_guess, word)
        print('\n')
        print('incorrectly guessed letters: ', incorrect_guess)
        letter=letter_choice()
        if letter in word:
            if letter in correct_guess:
                print('You have already used this letter! Try again')
            else:
                print('Yeey! Great job!')
                correct_guess += letter
        else:
            show_hangman_values[chances]= hangman_values[chances]
            chances +=1
            if letter in incorrect_guess:
                print('You have already used this letter. Try again!')
            else:    
                print("Bad luck! Try again, this letter doesn't exist inside the word")
                incorrect_guess += letter
    clear()

def main():
    print('Welcome to Hangman game! Guess the word:)')
    word_list= list(web2set)
    word=pick_random_word(word_list)
    print(word)
    check_letter(word)
   
main()


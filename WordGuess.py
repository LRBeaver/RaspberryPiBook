__author__ = 'lyndsay.beaver'

import random

words = ['chicken', 'dog', 'cat', 'chicken', 'cow']
lives_remaining = 14

def pick_a_word():
    word_position = random.randint(0, len(words)-1)
    return words[word_position]

print(pick_a_word())

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done')
            break
        if lives_remaining == 0:
            print('You are hung!')
            print('The word was: ' + word)
            break

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or the whole word?')
    return guess

def process_guess(guess, word):
    global lives_remaining
    lives_remaining = lives_remaining-1
    return False

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # letter found
            display_word = display_word + letter
        else:
            # letter not found
            display_word = display_word + '-'
    print display_word

play()

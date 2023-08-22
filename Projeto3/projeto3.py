#Hangman
import random
import string

from words import words_animal
from words import words_object
from words import words_action
from words import words_food

def get_animal_word(words_animal):
    word_animal = random.choice(words_animal)
    return word_animal

def get_object_word(words_object):
    word_object = random.choice(words_object)
    return word_object

def get_action_word(words_action):
    word_action = random.choice(words_action)
    return word_action

def get_food_word(words_food):
    word_food = random.choice(words_food)
    return word_food

def get_word(list_chosen):
    if list_chosen == 'a':
        word = get_animal_word(words_animal)
    elif list_chosen == 'o':
        word = get_object_word(words_object)
    elif list_chosen == 'ac':
        word = get_action_word(words_action)
    elif list_chosen == 'f':
        word = get_food_word(words_food)
    return word

def hangman(list_chosen):
    word = list_chosen.upper()
    word_letters = set(word) #Letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user guessed

    #getting user input
    while len(word_letters) > 0:
        #letters used
        print('You have used these letters: ', ' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already tested that letter. Try again')

        else:
            print('Invalid. Try again')
    print(f'You gessed it right! The word is {word}')


category = input('You can play hangman on four categories: animal (A), object (O), action (Ac) and food(F). Which one would you like? ').lower()
if category == 'a':
    list_chosen = get_word(category)
    hangman (list_chosen)
elif category == 'o':
    list_chosen = get_word(category)    
    hangman (list_chosen)
elif category == 'ac':
    list_chosen = get_word(category)
    hangman (list_chosen)
elif category == 'f':
    list_chosen = get_word(category)
    hangman (list_chosen)




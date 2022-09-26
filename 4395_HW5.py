# Homework 5
# lisa Chen

import sys
import pathlib
import nltk
import random
import string
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.stem.porter import *

# Function preprocess raw text to be returned for lexical diversity calculation
def preprocess_raw_text(raw_text):
    raw_text = raw_text.replace('\n', ' ') # gets rid of new line characters
    all_token = word_tokenize(raw_text)  # Tokenize lower-case raw text
    all_token = [t.lower() for t in all_token if t.isalpha()] # makes text lowercase
    # reduce tokens to those that are alpha, not in NLTK stopword list, and have length > 5
    all_token = [t for t in all_token if t.isalpha() and t not in stopwords.words('english') and len(t) > 5]

    # Lemmatize tokens
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in all_token]
    # set() used to make list of unique lemmas
    lemmas_unique = list(set(lemmas))

    # pos tagging on unique lemmas
    tags = nltk.pos_tag(lemmas_unique)
    # First 20 tagged items printed
    print(tags[:20])

    # Creates list of noun lemmas
    noun_words = [noun for (noun, pos) in tags if pos[0] == 'N']

    # Prints number of tokens after reduction
    print("\nFrom step A, number of tokens: " + len(all_token))
    # Prints number of nouns from list of noun lemmas
    print("\nNumber of nouns:" + len(noun_words))

    unique_token = set(lemmas_unique)  # unique token variable
    # Calculates lexical diversity of tokenized text and outputs it to 2 decimal places
    print("\nLexical diversity: %.2f" % (len(unique_token) / len(all_token)))

    # Returns tokens (not unique tokens) and nouns
    return all_token, noun_words

def guess_game(common_word_list):
    print("\nLet's play a word guessing game!")
    correct_guess = False # variable for if guess is correct

    # Gives user 5 points to start with
    score = 5

    # Randomly chooses 1 of the 50 words in the top 50 list
    selected_word = random.choice(common_word_list)

    # Outputs to console a underscore space for each letter in the word
    answer_list = []
    for i in range(len(selected_word)):
        answer_list.append("_")
    for i in answer_list:
        print(i, end=' ')

    # Ends game if score negative or if guess is ! or user guessed word
    while score > -1 and user_guess != "!" and answer_list != selected_word:
        # Asks user for a letter
        user_guess = input("\nGuess a letter:")
        # Prints Right! if guess is correct and fills in all matching letters _ with the guess
        for i in range(len(selected_word)):
            if user_guess == selected_word[i]:
                answer_list[i] = selected_word[i]
                correct_guess = True
        if correct_guess:
            print("\nRight! Score is " + score)
            score += 1 # adds 1 point to the score
            # prints out the word filled in with user guesses so far
            for i in answer_list:
                print(i, end=' ')
        else:
            # If guess incorrect, prints "Sorry, guess again"
            print("\nSorry, guess again. Score is " + score)
            score -= 1 # subtracts 1 point from score
            # prints out word filled in with user guesses so far
            for i in answer_list:
                print(i, end=' ')

    print("\nYou solved it!")
    print("\nCurrent score: " + score)

def main():
    # Gets the filename from a system argument and displays an error msg if there isn't one
    if len(sys.argv) > 1:
        arg_input = sys.argv[1] # system argument variable
        print("Input file name: ", arg_input) # prints the name of the file
        # reads in file
        with open(pathlib.Path.cwd().joinpath(arg_input), 'r') as f:
            text_in = f.read() # stores the read in raw text
    else:
        print("\nYou're missing the needed system argument.") # error msg
        print("\nThe program will now end.") # msg of ending program
        sys.exit() # stops the program

    all_token, noun_words = preprocess_raw_text(text_in) # calls preprocessing text function

    # Makes dictionary of {noun:count of noun in tokens} items from the nouns and tokens lists
    counts = {t: noun_words.count(t) for t in noun_words}
    # Sorts dict by count
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # Prints 50 most common words and their counts and saves printed words to list
    common_word_list = []
    for i in range(50):
       common_word_list.append(sorted_counts[i])
       print(sorted_counts[i])

    guess_game(common_word_list) # calls guess_game function

# Ensures the main function is run
if __name__ == '__main__':
    main() # calls the main method

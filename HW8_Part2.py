# Lisa Chen
# Homework 8 program 2

import sys
import pathlib
import re
import pickle
import math

#computes probability for test file lines
def compute_prob(line, eng_dict, french_dict, uni_new_en_dict, uni_new_french_dict):
    high_prob = 0 # probability marker variable
    prob = 1 # probability variable
    if len(eng_dict) * len(uni_new_en_dict):
        high_prob = 0
    elif len(french_dict) * len(uni_new_french_dict):
        high_prob = 1
    else:
        high_prob = 2
    return high_prob

# calculates probabilty of accuracy of classified instances
def file_accuracy(result):
    # opens langID file
    with open('langId.sol', 'r') as f:
        text = f.read()
    # opens results file
    with open('high_prob_result.txt', 'r') as r:
        results = r.read()
    # checks accuracy of results
    accur_percent = 100
    if text == results:
        print("Lines of incorrectly classified items: none")
    else:
        i = 0 # counter variable
        for line in results:
            for row in text:
                if line == row:
                    i += 1
                else:
                    print(i) # outputs the line numbers of the incorrectly classified items
                    accur_percent = accur_percent - 1
    print(accur_percent + "%") # prints % of correctly classified instances in the test set

if __name__ == '__main__':
    # reads in pickeled dictionaries
    with open('eng_dict.pickle', 'rb') as handle:
        new_en_dict = pickle.load(handle)
    with open('french_dict.pickle', 'rb') as handle_french:
        new_french_dict = pickle.load(handle_french)
    with open('italian_dict.pickle', 'rb') as handle_ital:
        new_italian_dict = pickle.load(handle_ital)
    with open('uni_eng_dict.pickle', 'rb') as handle:
        uni_new_en_dict = pickle.load(handle)
    with open('uni_french_dict.pickle', 'rb') as handle_french:
        uni_new_french_dict = pickle.load(handle_french)
    with open('uni_italian_dict.pickle', 'rb') as handle_ital:
        uni_new_italian_dict = pickle.load(handle_ital)

    result = open('high_prob_result.txt', 'w') # opens file to writes language with highest probability to a file
    f = open('langId.test', 'r') # opens test file
    # For each line in test file, calculates a probability for each language
    for line in f:
        high_prob = compute_prob(line, new_en_dict, new_french_dict,  uni_new_en_dict, uni_new_french_dict) # calls compute probability function
        if high_prob == 0:
            result.write("English\n") # write out english value
        elif high_prob == 1:
            result.write("French\n") # writes out french result
        else:
            result.write("Italian\n") # write out italian result

    file_accuracy(result) # calls file accuracy function

    result.close()  # closes file
    f.close()  # closes file



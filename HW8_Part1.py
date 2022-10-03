# Lisa Chen
# Homework 8 program 1

import sys
import pathlib
import re
import nltk
import pickle
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

# function handles processing the text and creating a dictionary for unigram and bigram
def dictionary_setup(training_file):
   # reads in text and removes newlines
   with open(training_file, "r", encoding = 'utf-8') as f:
      for line in f:
         line.strip()
      text = f.read()
   # tokenizes the text
   file_tokenize = word_tokenize(text)

   # uses nltk to create a bigram list
   tokens = text.split()
   bigrams = list(ngrams(tokens, 2))

   # uses nltk to create a unigram list
   unigrams = list(ngrams(tokens, 1))

   # uses bigram list to create bigram dictionary of bigrams and counts
   bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}

   # uses unigram list to create a unigram dictionary of unigrams and counts
   unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}

   # returns the unigram dictionary and bigram dictionary
   return unigram_dict, bigram_dict



if __name__ == '__main__':
   eng_file = "LangId.train.English"
   fre_file = "LangId.train.French"
   ital_file = "LangId.train.Italian"

   # Handles the english file
   unigram_dict, bigram_dict = dictionary_setup(eng_file) # calls the dictionary_setup function
   # Handles the french file
   french_unigram_dict, french_bigram_dict = dictionary_setup(fre_file) # calls the dictionary_setup function
   # Handles the italian file
   italian_unigram_dict, italian_bigram_dict = dictionary_setup(ital_file) # calls the dictionary_setup function

   # pickles the 6 dictionaries
   with open('eng_dict.pickle', 'wb') as handle:
      pickle.dump(bigram_dict, handle)
   with open('french_dict.pickle', 'wb') as handle:
      pickle.dump(french_bigram_dict, handle)
   with open('italian_dict.pickle', 'wb') as handle:
      pickle.dump(italian_bigram_dict, handle)
   with open('uni_eng_dict.pickle', 'wb') as handle:
      pickle.dump(unigram_dict, handle)
   with open('uni_italian_dict.pickle', 'wb') as handle:
      pickle.dump(french_unigram_dict, handle)
   with open('uni_italian_dict.pickle', 'wb') as handle:
      pickle.dump(italian_unigram_dict, handle)




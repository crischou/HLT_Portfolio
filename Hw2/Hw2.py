#Homework 2
#Cris Chou

import nltk
#nltk.download()
from nltk import word_tokenize
from nltk import sent_tokenize
import sys
import re
import pathlib
import os

#read file


#preprocess file
#def preprocess(text):
  #  text = text.lower()
    


    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please use valid file path: ")
        quit()

    fp = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(fp), 'r') as f:
        #tokenize file
        text_in = f.read()
        tokens = word_tokenize(text_in)

        #calculating lexical diversity
        #get total words
        total_words = len(tokens)
    
        #get unique words
        unique_words = len(set(tokens))

        #get lexical diversity
        lexical_diversity = unique_words/total_words
        print("Lexical Diversity: ", str(round(lexical_diversity,2)))

        #preprocess(text_in)
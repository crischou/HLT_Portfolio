#Cris Chou
#Homework 4


import nltk
from nltk import word_tokenize
from nltk import bigrams
from nltk import unigrams

#create a function witha filename as argument

def langMod(text_in):
    #read text and remove newlines
    text = open(text_in).read().replace('\n','')
    #tokenize text
    tokens = nltk.word_tokenize(text)
    #use nltk to create bigrams list
    bigrams = nltk.bigrams(tokens)
    #use nltk to create unigrams list
    unigrams = nltk.unigrams(tokens)
    
#Cris Chou
#Homework 4

import sys
import pathlib

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

    #use the bigram list to create bigram dict with counts
    bigram_dict = {}
    for bigram in bigrams:
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1

    #do same thing with unigram
    unigram_dict = {}
    for unigram in unigrams:
        if unigram in unigram_dict:
            unigram_dict[unigram] += 1
        else:
            unigram_dict[unigram] = 1
    
    #return bigram and unigram dicts
    return bigram_dict, unigram_dict

 

if __name__ == '__main__':
    
    #function call on training files

    bidictEn, unidictEn = langMod('/data/LangId.train.English')
    bidictFr, unidictFr = langMod('/data/LangId.train.French')
    bidictIt, unidictIt = langMod('/data/LangId.train.Italian')
    
#Cris Chou
#Homework 4

import sys
import pathlib

import nltk
from nltk import word_tokenize
from nltk.util import ngrams

import pickle

#create a function witha filename as argument

def langMod(text_in):
    #read text and remove newlines
    tokens = open(text_in).read().replace('\n','')
    #tokenize text
    unigrams = nltk.word_tokenize(text_in)
    #use nltk to create bigrams list
    bigrams = list(ngrams(tokens,2))
    #use nltk to create unigrams list
    #unigrams = nltk.unigrams(tokens)

    #use the bigram list to create bigram dict with counts
    bigram_dict = {}
    bigram_dict = {b:bigrams.count(b) for b in set(bigrams)}

    #do same thing with unigram
    unigram_dict = {}
    unigram_dict = {u:unigrams.count(u) for u in set(unigrams)}
    
    #return bigram and unigram dicts
    return bigram_dict, unigram_dict
    
    

if __name__ == '__main__':
    
    #function call on training files

    bidictEn, unidictEn = langMod('data\LangId.train.English')
    bidictFr, unidictFr = langMod('data\LangId.train.French')
    bidictIt, unidictIt = langMod('data\LangId.train.Italian')

    #pickle dicts
    pickle.dump(bidictEn, open('bidictEn.p', 'wb'))
    pickle.dump(unidictEn, open('unidictEn.p', 'wb'))
    pickle.dump(bidictFr, open('bidictFr.p', 'wb'))
    pickle.dump(unidictFr, open('unidictFr.p', 'wb'))
    pickle.dump(bidictIt, open('bidictIt.p', 'wb'))
    pickle.dump(unidictIt, open('unidictIt.p', 'wb'))



    

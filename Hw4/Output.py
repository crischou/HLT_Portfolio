#Cris Chou
#Homework 4

import pickle
from nltk.util import ngrams
from nltk import word_tokenize
import math


#get pickled dicts
bidictEn = pickle.load(open('bidictEn.p', 'rb'))
unidictEn = pickle.load(open('unidictEn.p', 'rb'))
bidictFr = pickle.load(open('bidictFr.p', 'rb'))
unidictFr = pickle.load(open('unidictFr.p', 'rb'))
bidictIt = pickle.load(open('bidictIt.p', 'rb'))
unidictIt = pickle.load(open('unidictIt.p', 'rb'))

#open test file
test = open('data\LangId.test')

#probablility of each language
def compute_prob(text_in, unigram_dict, bigram_dict, N, V):
    #N = number of tokens in training data
    #V = unique tokens in training data

    unigrams_test = word_tokenize(text_in)
    bigrams_test = list(ngrams(unigrams_test,2))

    #p of using a variation of laplace smoothing

    p_gt = 1
    p_laplace = 1 

    for bigram in bigrams_test:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        n_gt = bigram_dict[bigram] if bigram in bigram_dict else 1/N
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        if d == 0:
            p_gt *= 1/N
        else:
            p_gt *= n_gt/d
            
        p_laplace *= ((n+1)/(d+V))
        
    print("Probability with laplace smoothing is %.5f" % (p_gt))


    
    
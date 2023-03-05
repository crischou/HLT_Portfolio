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


#probablility of each language
def compute_prob(text_in, unigram_dict, bigram_dict, V):
    #V = vocab size
    unigrams_test = word_tokenize(text_in)
    bigrams_test = list(ngrams(unigrams_test,2))
    
    #print(bigrams_test)
    #print(unigram_dict)
    #p of using a variation of laplace smoothing
    p_laplace = 1 

    for bigram in bigrams_test:

        
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0

        p_laplace *= ((n+1)/(d+V))
    
    #print(p_laplace)
    #print("Probability with laplace smoothing is %.5f" % p_laplace)
    
    return p_laplace

    
if __name__ == '__main__':

    #get vocab size
    vocab_size = len(unidictEn) + len(unidictFr) + len(unidictIt)
    print(vocab_size)


    check = []
    count = 0
    with open('data\LangId.test') as f:
            lines = f.readlines()

            for line in lines:
                en_prob = compute_prob(line, unidictEn, bidictEn, vocab_size)
                fr_prob = compute_prob(line, unidictFr, bidictFr, vocab_size)
                it_prob = compute_prob(line, unidictIt, bidictIt, vocab_size)

                #find out which one is most likely
                if en_prob > fr_prob and en_prob > it_prob:
                    check.append("English")
                elif fr_prob > en_prob and fr_prob > it_prob:
                    check.append("French")
                elif it_prob > en_prob and it_prob > fr_prob:
                    check.append("Italian")
                else:
                    check.append("Unknown")
                
    total = len(check)
    correct = 0
    #check for accuracy
    with open('data\LangId.sol') as f:

        lines = f.readlines()
        for i in range(len(lines)):
            #remove the numbers to compare
            if lines[i].strip()[2:] == check[i]:
                correct += 1
            print(lines[i].strip()[2:], " ", check[i])
            if i == 50:
                break
    print("Accuracy is %.2f" % (correct/total))
    

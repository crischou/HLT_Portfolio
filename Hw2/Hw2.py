#Homework 2
#Cris Chou

import nltk
#nltk.download()
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
import sys
import re
import pathlib
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint

#preprocess file
def preprocess(text_in):
    #remove punctuation, make lowercase
    text_in = re.sub(r'[.?,:;()\-\n\d]', ' ', text_in.lower())
    #tokenize
    tokens = word_tokenize(text_in)
    #remove stopwords and make sure words are longer than 5 characters
    stop_words = (stopwords.words('english'))
    uniq_tokens = [t for t in tokens if not t in stop_words and len(t) > 5]
    
    #lemmatize
    wnl = WordNetLemmatizer()
    lematized = [wnl.lemmatize(t) for t in uniq_tokens]
    #get unique lemmas
    lema_tokens = set(lematized)
    #get pos tags
    pos_tags = nltk.pos_tag(lema_tokens)
    #print first 20
    print(pos_tags[:20])
    #create list of nouns
    nouns = [t[0] for t in pos_tags if t[1] == 'NN']
    #print initial token amount
    print("Unique token amount: ", len(uniq_tokens))
    #print number of nouns
    print("Number of nouns: ", len(nouns))
    print(len(tokens))
    #return total tokens, and nouns
    return tokens, nouns

#guessing game function
def guess_game(top_50):
    points = 5
    print("Let's play a guessing game!")
    #initialize seed
    seed()
    #choose random noun
    rand = randint(0,49)
    word = top_50[rand]
    display = "_" * len(word)
    #get user input
    print(display)
    guess = input("Guess a letter: ")



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

        tokens, nouns = preprocess(text_in)

        #making dictonary of {noun: count of noun in tokens}
        noun_dict = {}
        for noun in nouns:
            noun_dict[noun] = tokens.count(noun)
        
        
        #sort top 50 and their counts
        sorted_nouns = sorted(noun_dict.items(), key=lambda x: x[1], reverse=True)
        print(sorted_nouns[:50])

        #make a list of top 50 nouns
        top_50 = [t[0] for t in sorted_nouns[:50]]

        #guessing game
        guess_game(top_50)


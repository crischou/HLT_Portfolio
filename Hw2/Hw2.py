import nltk
nltk.download()
from nltk import word_tokenize
from nltk import sent_tokenize
import sys


#read file


#preprocess file
def preprocess(file):
    print("Hello")


    
if __name__ == 'main':
    if(sys.argv) > 2:
        print("Please use valid file path: ")
        quit()

        fp = sys.argv[1]
        with open(pathlib.Path.cwd() / fp) as f:
            
            text_in = f.read()
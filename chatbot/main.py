#Cris Chou
#Chat bot


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

class Chatbot:
    def __init__(self):
        self.users = {}
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def chat(self):
        name = input("Hello, what is your name? ")
        #check if new user or returning user
        if name not in self.users:
            self.users[name] = {}
            self.greet(name)

        elif name in self.users:
            print("Welcome back, " + name + "!")



    def greet(self, name):
        greetings = ["Hello","Hi","Hey","Howdy", "What's up","How are you doing"]
        print(random.choice(greetings) + " " + name + "!")
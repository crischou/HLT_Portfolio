#Cris Chou
#Chat bot


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random
from nltk.sentiment import SentimentIntensityAnalyzer


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

        while True:
            message = input("You: ")
            #self.users[name][message].append(message)


            if "bye" in message.lower():
                self.goodbye(name)
                break
            else:
                response = self.generate_response(name,message)
                print("Chatbot: " + response)


    def greet(self, name):
        greetings = ["Hello","Hi","Hey","Howdy", "What's up","How are you doing"]
        print(random.choice(greetings) + " " + name + "!")

    def goodbye(self, name):
        goodbyes = ["Goodbye","Bye","See you later","See you next time", "Have a good day"]
        print(random.choice(goodbyes) + " " + name)

    def generate_response(self, name, message):
        #sentiment analysis
        sentAnalyzer = SentimentIntensityAnalyzer()
        
        sentiment = sentAnalyzer.polarity_scores(message)

        if sentiment['compound'] > 0.5:
            return "Thats great!"
        elif sentiment['compound'] < -0.5:
            return "I'm sorry to hear that."
        else:
            return "Sorry, I don't really know what to say."


chatbot = Chatbot()
chatbot.chat()
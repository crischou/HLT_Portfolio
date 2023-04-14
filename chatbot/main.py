#Cris Chou
#Chat bot


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random
from nltk.sentiment import SentimentIntensityAnalyzer
import re

class Chatbot:

    def __init__(self):
        self.users = {}
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def chat(self):

        #pattern for grade/year
        grade_pattern = r'freshmen|sophmore|junior|senior'

        name = input("Hello, what is your name? ")
        #check if new user or returning user
        if name not in self.users:
            self.users[name] = {'name': name, 'grade': [], 'messages': [], 'responses': [], 'sentiment': []}
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
                #check if user states their grade/year
                match = re.search(grade_pattern,message,re.IGNORECASE)
                if match:
                    grade = self.grade(name,match.group(0))

                if("grade" in message.lower() or "year" in message.lower()):
                    if len(self.users[name]['grade']) == 0:
                        print("You haven't told me your grade yet.")
                    else:
                        print("You are a " + self.users[name]['grade'][0] + " at UTD.")
               
                else:    
                    response = self.generate_response(name,message)
                    print("Chatbot: " + response)
                


    #greetings
    def greet(self, name):
        greetings = ["Hello","Hi","Hey","Howdy", "What's up","How are you doing"]
        print(random.choice(greetings) + " " + name + "!")
    #goodbyes
    def goodbye(self, name):
        goodbyes = ["Goodbye","Bye","See you later","See you next time", "Have a good day"]
        print(random.choice(goodbyes) + " " + name)

    #keep track of user grades
    def grade(self, name,grade):
        self.users[name]['grade'].append(grade)

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

cont = True
while cont:
    chatbot.chat()
    ans = input("Would you like to chat again? (y/n): ")
    if ans == "n":
        cont = False
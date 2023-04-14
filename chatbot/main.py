#Cris Chou
#Chat bot


import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import os

from langchain import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from camo import API_KEY


os.environ['OPENAI_API_KEY'] = API_KEY

#Using langchains VectorstoreIndexCreator
loader = TextLoader("data/data_l.txt")
index = VectorstoreIndexCreator().from_loaders([loader])


class Chatbot:

    def __init__(self):
        self.users = {}
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def chat(self):
        
        like_keywords = ["like","love","enjoy","want","favorite","prefer"]
        dislike_keywords = ["dislike","hate","dont like","dont enjoy","dont want"]
        #pattern for grade/year
        grade_pattern = r'freshmen|sophmore|junior|senior'
        like_pattern = r'\b(?:%s)\b' % '|'.join(like_keywords)
        dislike_pattern = r'\b(?:%s)\b' % '|'.join(dislike_keywords)

        name = input("Chatbot: Hello, what is your name? ")
        #check if new user or returning user
        if name not in self.users:
            self.users[name] = {'name': name, 'grade': [],'message': [],'responses': [],"questions": [],"likes": [],"dislikes": []}
            self.greet(name)

        elif name in self.users:
            print("Chatbot: Welcome back, " + name + "!")

        
        while True:
            message = input("You: ")
            self.users[name]['message'].append(message)

            if "bye" in message.lower():
                self.goodbye(name)
                break
            else:
                #check if user states their grade/year
                match = re.search(grade_pattern,message,re.IGNORECASE)
                if match:
                    self.grade(name,match.group(0))
                
                if("grade" in message.lower() or "year" in message.lower()):
                    if len(self.users[name]['grade']) == 0:
                        print("You haven't told me your grade yet.")
                    #if multiple grade values get latest one
                    elif len(self.users[name]['grade']) > 1:
                        print("You are a " + self.users[name]['grade'][len(self.users[name]['grade'])-1])
                    else:
                        print("You are a " + self.users[name]['grade'][0])
                #Keep track of user questions
                elif(self.isQuestion(message)):
                    #print("this is a question")
                    #using LangChain query to get response
                    response = index.query(message)
                    print("Chatbot: " + response)
                    
                    self.users[name]['questions'].append(message)

                #keep track of user likes
                elif(re.search(like_pattern,message,re.IGNORECASE)):
                    matches = re.findall(like_pattern,message,flags = re.IGNORECASE)
                    for match in matches:
                        like = re.findall(f'{match}(/w+)',message,flags = re.IGNORECASE)
                        print(like)
                        self.users[name]['likes'].append(like)

                    print("Chatbot: " + "Noted. "+name+" likes ")
                    for like in self.users[name]['likes']:
                        print(like," and ")
                    
                else:    
                    response = self.sent_response(name,message)
                    print("Chatbot: " + response)
                

    #check if message is a question
    def isQuestion(self,message):
        message = message.lower()
        if "?" in message:
            return True
        elif "who" in message or "what" in message.lower or "when" in message or "where" in message or "why" in message or "how" in message:
            return True
        else:
            return False
        
    

    #greetings
    def greet(self, name):
        greetings = ["Hello","Hi","Hey","Howdy", "What's up","How are you doing"]
        print("Chatbot: "+ random.choice(greetings) + " " + name + "!")
    #goodbyes
    def goodbye(self, name):
        goodbyes = ["Goodbye","Bye","See you later","See you next time", "Have a good day"]
        print("Chatbot: " + random.choice(goodbyes) + " " + name)

    #keep track of user grades
    def grade(self, name,grade):
        self.users[name]['grade'].append(grade)

    #sentiment response
    def sent_response(self, name, message):
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
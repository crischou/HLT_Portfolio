#Cris Chou
#Chatbot


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
        
        #like and disklike keywords
        like_keywords = ["like","love","enjoy","want","favorite","prefer"]
        dislike_keywords = ["dislike","hate","dont like","dont enjoy","dont want","don't like","dont like"]
        #pattern for grade/year
        grade_pattern = r'freshmen|sophmore|junior|senior'
        #pattern for like and dislike keywords
        like_pattern = r'\b(?:%s)\b' % '|'.join(like_keywords)
        dislike_pattern = r'\b(?:%s)\b' % '|'.join(dislike_keywords)
        #school related keywords
        school_keywords = ["utd","university of texas at dallas","college","school","university","utdallas","class","student","professor","grades","semester","enrollment","degree","major","minor","graduate","undergraduate","graduate school","undergraduate school","graduate student"]
        #thank keywords
        thanks_keywords = ["thank","thanks","thank you","thanks you","appreciate","appreciate it","appreciate you","appreciate it"]
        #greeting keywords
        greetings_keywords = ["hi","hello","howdy","salutations","hey","yo","sup"]
        #name pattern
        name_pattern = re.compile(r"(i'm|i am|im|my name is|my names)[\s]+([A-Za-z]+)",re.IGNORECASE)

        print("Chatbot: Hello, what is your name?")
        raw_in = input("You: ")
        match = re.search(name_pattern,raw_in)
        if match:
            name = match.group(2)
        else:
            name = raw_in
                    
        #check if new user or returning user
        if name not in self.users:
            self.users[name] = {'name': name, 'grade': [],'message': [],'responses': [],"questions": [],"likes": [],"dislikes": []}
            self.greet(name)

        elif name in self.users:
            print("Chatbot: Welcome back, " + name + "!")

        
        while True:
            message = input("You: ")
            self.users[name]['message'].append(message)

            #tokenize message
            tokens = nltk.word_tokenize(message)
            #get pos tags
            pos = nltk.pos_tag(tokens)
            #get subject of message
            ner_tags = nltk.ne_chunk(pos)
            subject = ""
            #extract subject
            for chunk in ner_tags:
                if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                    subject = ' '.join(c[0] for c in chunk.leaves())
                    break

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
                    

                    #using LangChain query to get response if related to utd
                    if (any(word in message.lower() for word in school_keywords)):
                        response = index.query(message)
                        print("Chatbot: " + response)
                    #check if asking about likes
                    elif(re.search(like_pattern,message,re.IGNORECASE)):
                        #check who the user is asking about
                        if subject == name or subject.lower() == "i":
                            #check if user has likes
                            if len(self.users[name]['likes']) == 0:
                                print("You haven't told me what you like yet.")
                            else:
                                #choose random like
                                #like = random.choice(self.users[name]['likes'])
                                like_items = ""
                                for likes in self.users[name]['likes']:
                                    like_items = like_items + ", "+ likes[0] 
                                print("Chatbot: "+name+" likes "+like_items)
                        #check if subject has likes
                        elif(subject in self.users):
                            if(len(self.users[subject]['likes'])> 0):
                                like_items = ""
                                for likes in self.users[subject]['likes']:
                                    like_items = like_items + ", "+ likes[0] 
                                print("Chatbot: "+subject+" likes "+like_items)
                            elif(len(self.users[subject]['likes']) == 0):
                                print("Chatbot: "+subject+" hasn't told me what they like yet.")
                        else:
                            print("Chatbot: I don't know who "+subject+" is.")

                            
                    elif(re.search(dislike_pattern,message,re.IGNORECASE)):
                        #check who the user is asking about
                        if subject == name:
                            #check if user has dislikes
                            if len(self.users[name]['dislikes']) == 0:
                                print("You haven't told me what you dislike yet.")
                            else:
                                #choose random dislike
                                #dislike = random.choice(self.users[name]['dislikes'])
                                dislike_items=""
                                for dislike in self.users[name]['dislikes']:
                                    dislike_items = dislike_items + ", "+ dislike[0] 
                                print("Chatbot: "+name+" dislikes "+ dislike_items)
                        #check if subject has likes
                        elif(subject in self.users):
                            if(len(self.users[subject]['dislikes'])> 0):
                                dislike_items = ""
                                for dislikes in self.users[subject]['dislikes']:
                                    dislike_items = dislike_items + ", "+ dislikes[0] 
                                print("Chatbot: "+subject+" dislikes "+dislike_items)
                            elif(len(self.users[subject]['dislikes']) == 0):
                                print("Chatbot: "+subject+" hasn't told me what they dislike yet.")
                        else:
                            print("Chatbot: I don't know who "+subject+" is.")
                    
                    self.users[name]['questions'].append(message)

                #keep track of user likes
                elif(re.search(like_pattern,message,re.IGNORECASE)):
                    
                    #looking for keywords
                    matches = re.findall(like_pattern,message,flags = re.IGNORECASE)
                    for match in matches:
                        likes = re.findall(f'{match} ([\w\s]+)',message,flags = re.IGNORECASE)
                        
                        self.users[name]['likes'].append(likes)

                    #print(len(self.users[name]['likes']))
                    print("Chatbot: " + "Noted. "+name+" likes "+likes[0])
                    
                #keep track of user dislikes
                elif(re.search(dislike_pattern,message,re.IGNORECASE)):
                    
                    #looking for keywords
                    matches = re.findall(dislike_pattern,message,flags = re.IGNORECASE)
                    for match in matches:
                        dislikes = re.findall(f'{match} ([\w\s]+)',message,flags = re.IGNORECASE)
                        
                        self.users[name]['dislikes'].append(dislikes)

                    #print(len(self.users[name]['dislikes']))
                    print("Chatbot: " + "Noted. "+name+" dislikes "+dislikes[0])
                #respond to user thanks
                elif(any(word in message.lower() for word in thanks_keywords)):
                    self.resp_ty(name)
                #respond to user greetings
                elif(any(word in message.lower() for word in greetings_keywords)):
                    self.greet(name)

                #general sentiment response
                else:    
                    response = self.sent_response(name,message)
                    print("Chatbot: " + response)
                

    #check if message is a question
    def isQuestion(self,message):
        message = message.lower()
        if "?" in message:
            return True
        elif "who" in message or "what" in message or "when" in message or "where" in message or "why" in message or "how" in message:
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

    #respond to thanks
    def resp_ty(self,name):
        responses = ["You're welcome","No problem","Anytime", "My pleasure", "No worries", "Of course"]
        print("Chatbot: " + random.choice(responses) + " " + name)

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
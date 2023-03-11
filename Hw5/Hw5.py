#Cris Chou
#Homework 5



from bs4 import BeautifulSoup

import urllib as ul

from nltk.tokenize import sent_tokenize

from urllib.request import Request, urlopen
from nltk import word_tokenize
from nltk.corpus import stopwords
import math


#choose a website with 15 external urls
url = 'https://en.wikipedia.org/wiki/Pattern_recognition_(psychology)'


def webCrawl(url): 
    
    res = ul.request.urlopen(url)
    text = res.read().decode('UTF-8')
    soup = BeautifulSoup(text, 'html5lib')
    counter = 0
    #get first 15 links from wikipage
    for links in soup.find_all('a'):
        link = links.get('href')
        
        #make sure they are not wiki links, and readable
        if 'wiki' not in link and 'http' in link and 'doi' not in link and 'extension' not in link:
            print(link)
            sentances= scrape(link)
            counter += 1
            #write to different file each time
            with open('link'+str(counter)+'.txt', 'w') as f:
                f.write(link)
                f.write('\n')
                #f.write(sentances)
                for sentance in sentances:
                    f.write(sentance)
                    f.write('\n')  
        if counter >= 15:
             break
        
def scrape(url):
    #get text from link and add to file
    #res = ul.request.urlopen(url)
    res = Request(url, headers={'User-Agent': 'Edg/110.0.1587.63'})

    text = urlopen(res).read().decode('UTF-8')
    soup = BeautifulSoup(text, 'html.parser')

    #get text
    ptags = soup.find_all('p')
    
    content = ''
    for line in ptags:
        content += line.get_text()+'\n'

    #delete new lines and and tabs
    #ptags = "".join(ptags)
    #ptags = ptags.replace('\n', '')
    #ptags = ptags.replace('\t', '')
    
    
    #get sentances with nltk sentance tokenizer
    sentances = sent_tokenize(content)
    
    return sentances
    
#function to extract 25 important terms from each link
def filter(file):

    with open(file, 'r') as f:
        text = f.read().lower()
        text = text.replace('\n', ' ')
        return text

#tf based on mazidi notebook
def create_tf_dict(file): 
    stop = stopwords.words('english')
    tf_dict = {}
    tokens = word_tokenize(file)
    tokens = [w for w in tokens if w.isalpha() and w not in stop]

    for t in tokens:
        if t in tf_dict:
            tf_dict[t] += 1
        else:
            tf_dict[t] = 1

    token_set = set(tokens)
    tf_dict = {t:tokens.count(t) for t in token_set}

    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t]/len(tokens)
    
    return tf_dict

#tf-idf based on mazidi notebook
def create_tfidf(tf, idf):
    tf_idf = {}
    for t in tf.keys():
        tf_idf[t] = tf[t] * idf[t]

    return tf_idf

webCrawl(url)
link1 = filter('link1.txt')
link2 = filter('link2.txt')
link3 = filter('link3.txt')
link4 = filter('link4.txt')
link5 = filter('link5.txt')
link6 = filter('link6.txt')
link7 = filter('link7.txt')
link8 = filter('link8.txt')
link9 = filter('link9.txt')
link10 = filter('link10.txt')
link11 = filter('link11.txt')
link12 = filter('link12.txt')
link13 = filter('link13.txt')
link14 = filter('link14.txt')
link15 = filter('link15.txt')

#creating tf dictionaries for each link
tf1 = create_tf_dict(link1)
tf2 = create_tf_dict(link2)
tf3 = create_tf_dict(link3)
tf4 = create_tf_dict(link4)
tf5 = create_tf_dict(link5)
tf6 = create_tf_dict(link6)
tf7 = create_tf_dict(link7)
tf8 = create_tf_dict(link8)
tf9 = create_tf_dict(link9)
tf10 = create_tf_dict(link10)
tf11 = create_tf_dict(link11)
tf12 = create_tf_dict(link12)
tf13 = create_tf_dict(link13)
tf14 = create_tf_dict(link14)
tf15 = create_tf_dict(link15)

vocab = set(tf1.keys())
vocab = vocab.union(set(tf2.keys()))
vocab = vocab.union(set(tf3.keys()))
vocab = vocab.union(set(tf4.keys()))
vocab = vocab.union(set(tf5.keys()))
vocab = vocab.union(set(tf6.keys()))
vocab = vocab.union(set(tf7.keys()))
vocab = vocab.union(set(tf8.keys()))
vocab = vocab.union(set(tf9.keys()))
vocab = vocab.union(set(tf10.keys()))
vocab = vocab.union(set(tf11.keys()))
vocab = vocab.union(set(tf12.keys()))
vocab = vocab.union(set(tf13.keys()))
vocab = vocab.union(set(tf14.keys()))
vocab = vocab.union(set(tf15.keys()))

print(len(vocab))



#idf based on mazidi notebook
idf_dict = {}

vocab_by_topic = [tf1.keys(), tf2.keys(), tf3.keys(), tf4.keys(), tf5.keys(), tf6.keys(), tf7.keys(), tf8.keys(), tf9.keys(), tf10.keys(), tf11.keys(), tf12.keys(), tf13.keys(), tf14.keys(), tf15.keys()]

for term in vocab:
    temp = ['x' for voc in vocab_by_topic if term in voc]
    idf_dict[term] = math.log(len(vocab_by_topic)/len(temp))

#tf-idf for each link
tfidf1 = create_tfidf(tf1, idf_dict)
tfidf2 = create_tfidf(tf2, idf_dict)
tfidf3 = create_tfidf(tf3, idf_dict)
tfidf4 = create_tfidf(tf4, idf_dict)
tfidf5 = create_tfidf(tf5, idf_dict)
tfidf6 = create_tfidf(tf6, idf_dict)
tfidf7 = create_tfidf(tf7, idf_dict)
tfidf8 = create_tfidf(tf8, idf_dict)
tfidf9 = create_tfidf(tf9, idf_dict)
tfidf10 = create_tfidf(tf10, idf_dict)
tfidf11 = create_tfidf(tf11, idf_dict)
tfidf12 = create_tfidf(tf12, idf_dict)
tfidf13 = create_tfidf(tf13, idf_dict)
tfidf14 = create_tfidf(tf14, idf_dict)
tfidf15 = create_tfidf(tf15, idf_dict)


#union all the tfidf and get the top 35 terms
tfidf = {}
tfidf.update(tfidf1)
tfidf.update(tfidf2)
tfidf.update(tfidf3)
tfidf.update(tfidf4)
tfidf.update(tfidf5)
tfidf.update(tfidf6)
tfidf.update(tfidf7)
tfidf.update(tfidf8)
tfidf.update(tfidf9)
tfidf.update(tfidf10)
tfidf.update(tfidf11)
tfidf.update(tfidf12)
tfidf.update(tfidf13)
tfidf.update(tfidf14)
tfidf.update(tfidf15)

#wordList = ''
#get combined weighted terms
combined_weighted_terms = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)[:35]
for term in combined_weighted_terms:
    print(term, '\n')
    #wordList += str(term[0])+', '


import pickle
#simple knowledge base
import spacy

nlp = spacy.load('en_core_web_md')

doc = nlp(link12)
knowledgeBase = {}

for ent in doc.ents:
    print(ent.text, ent.label_)
    knowledgeBase[ent.text] = ent.label_

#pickle knowledge base
pickle.dump(knowledgeBase, open('knowledgeBase.p', 'wb'))


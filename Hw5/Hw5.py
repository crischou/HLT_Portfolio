#Cris Chou
#Homework 5



from bs4 import BeautifulSoup
import requests
import urllib as ul
import wikipedia
from nltk.tokenize import sent_tokenize
import re
from urllib.request import Request, urlopen

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
    

webCrawl(url)
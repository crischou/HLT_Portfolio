#Cris Chou
#Homework 5



from bs4 import BeautifulSoup
import requests
import urllib as ul
import wikipedia

#choose a website with 15 external urls
url = 'https://en.wikipedia.org/wiki/Three-body_problem'


def webCrawl(url): 
    #loop through urls
    for i in range(15):
        res = ul.request.urlopen(url)
        text = res.read().decode('UTF-8')
        soup = BeautifulSoup(text, 'html5lib')
        #scrape text from each url and put into a file
        with open('webCrawl.txt', 'a') as f:
            f.write(soup.get_text())
            

webCrawl(url)
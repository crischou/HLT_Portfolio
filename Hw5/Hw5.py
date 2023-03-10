#Cris Chou
#Homework 5



from bs4 import BeautifulSoup
import requests
import urllib as ul
import wikipedia

#choose a website with 15 external urls
url = 'https://en.wikipedia.org/wiki/Three-body_problem'


def webCrawl(url): 
    
    res = ul.request.urlopen(url)
    text = res.read().decode('UTF-8')
    soup = BeautifulSoup(text, 'html5lib')
    counter = 0
    #get first 15 links from wikipage
    for links in soup.find_all('a'):
        link = links.get('href')

        #make sure they are not wiki links
        if 'wiki' not in link and 'http' in link:
            print(link)
            counter += 1
            #write to different file each time
            with open('link'+str(counter)+'.txt', 'w') as f:
                f.write(link)
                f.write('\n')

        if counter >= 15:
             break
        #write to file
        

webCrawl(url)
import parse2csv as parse2csv
from newspaper import Article
import requests

src = 'mlcentre'
data = []

'''
check_link - function to check the existence of a link

Arguments: 
    link - url of the current article

Libraries:
    requests
'''
def check_link(link):
    response = requests.get(link)
    
    # Site status = response[200] (available)
    if str(response) == '<Response [200]>':
        return 1
    
    return 0
        
'''
parse_mlcentre - function for parsing from the Mlcentre website

Libraries:
    newspaper: pip install newspaper3k; pip install lxml-html-clean
'''
def parse_mlcentre():
    url = 'https://mlcentre.ru/articles/'

    # Enumeration of possible options for article numbers
    for iter in range(100000, 1000000):
        curData = []
        curUrl = url + str(iter)
    
        # Parsing data if the site is available
        if(check_link(curUrl)):
            # Saving data to a dataset
            curData.append(src)
            curData.append(curUrl)
            curData.append('data/' + str(iter) + '.txt')

            # Parsing data from the site
            article = Article(curUrl)
            article.download()
            article.parse()

            # Writing an article to a text file
            f = open('data/' + str(iter) + '.txt', 'w+')
            f.write(article.title + '\n')

            for s in article.text:
                f.write(s)

            f.close()

            print("Yes", iter)
            data.append(curData)

parse_mlcentre()
parse2csv.data2csv(data, src)
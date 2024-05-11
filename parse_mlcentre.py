import os
import requests
import parse2csv as parse2csv
from newspaper import Article

src = 'mlcentre'

'''
check_link - function to check the existence of a link

Arguments: 
    link - url of the current article

Libraries:
    requests
'''
def check_link(link):
    try:
        response = requests.get(link)
    except:
        return 0
    
    # Site status = response[200] (available)
    if str(response) == '<Response [200]>':
        return 1
    
    return 0
        
'''
parse_mlcentre - function for parsing from the Mlcentre website

Libraries:
    newspaper: pip install newspaper3k; pip install lxml-html-clean
'''
def parse_mlcentre(data, sites_cnt):
    url = 'https://mlcentre.ru/articles/'

    path = os.getcwd()
    os.chdir(path)
    if not(os.path.isdir('mlcentre')):
        os.mkdir('mlcentre')

    # Enumeration of possible options for article numbers
    for iter in range(100000, 100000+sites_cnt):
        curData = []
        curUrl = url + str(iter)
    
        # Parsing data if the site is available
        if(check_link(curUrl)):
            # Saving data to a dataset
            curData.append(src)
            curData.append(curUrl)
            curData.append('mlcentre/' + str(iter) + '.txt')

            # Parsing data from the site
            article = Article(curUrl)
            article.download()
            article.parse()

            # Writing an article to a text file
            f = open('mlcentre/' + str(iter) + '.txt', 'w+')
            f.write(article.title + '\n')

            for s in article.text:
                f.write(s)

            f.close()

            print("Yes", iter)
            data.append(curData)
        else:
            print('Skip', iter)

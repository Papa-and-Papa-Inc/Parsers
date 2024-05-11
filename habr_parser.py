from newspaper import Article
import os

def habr_parser():
    url = 'https://habr.com/articles/'

    data = []

    path = os.getcwd()
    os.chdir(path)
    if not(os.path.isdir('habr')):
        os.mkdir('habr')

    i = 1
    while i < 1000:
        try:
            link = url + f'{i}'
            article = Article(link)
            article.download()
            article.parse()
            text = article.text
            if (text != ''):
                rel_path = f'/habr/{i}.txt'
                file = open(path+rel_path, '+w')
                file.write(text)
                file.close() 
                data.append(["habr", link, rel_path])
                print("SUCCESS:", link)
            else:
                print('TOO OLD! -- ' + link)
        except:
            print("There is no page:", link)    

    
        i+=1
    
    return data


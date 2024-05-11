import pandas as pd
import glob

'''
data2csv - function for converting a data array into csv format

Arguments: 
    data - an array with site data like: src, link, content
    src - a string containing information about the site from which the articles were parsed (only title, without domain)

Libraries:
    pandas: pip install pandas
'''
def data2csv(data, src):
    df = pd.DataFrame(data)
    df.to_csv(src + '.csv', sep='\t')

    return

'''
merge_csv - function for merging csv files

Libraries:
    pandas: pip install pandas
    glob
'''
def merge_csv():
    csvFiles = glob.glob('*.{}'.format('csv'))
    print(csvFiles)
    mergedCSV = []

    for file in csvFiles:
        df = pd.read_csv(file)
        mergedCSV.append(df)

    df = pd.concat(mergedCSV, ignore_index=True)
    df.to_csv('articles.csv')

    return
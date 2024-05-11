import pandas as pd
import glob

def data2csv(data, src):
    df = pd.DataFrame(data)
    df.to_csv(src + '.csv', sep='\t')

def merge_csv():
    csvFiles = glob.glob('*.{}'.format('csv'))
    mergedCSV = pd.DataFrame()

    for file in csvFiles:
        df = pd.read_csv(file)
        mergedCSV = mergedCSV.append(df, ignore_index=True)

    df.to_csv('articles.csv', sep='\t')

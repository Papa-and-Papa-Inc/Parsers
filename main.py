import os
from threading import Thread
from habr_parser import habr_parser
from parse_mlcentre import parse_mlcentre
from parse2csv import data2csv, merge_csv

def main():
    habr_data = []
    mlcentre_data = []

    thread_habr = Thread(target = habr_parser, args = [habr_data, 50])
    thread_mlcentre = Thread(target = parse_mlcentre, args = [mlcentre_data, 50])

    thread_habr.start()
    thread_mlcentre.start()

    thread_habr.join()
    thread_mlcentre.join()

    if not(os.path.isdir('csv')):
        os.mkdir('csv')
    os.chdir('csv')

    data2csv(habr_data, 'habr')
    data2csv(mlcentre_data, 'mlcentre')

    merge_csv()

    return

if __name__ == "__main__":
    main()
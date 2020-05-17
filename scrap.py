#!/usr/bin/python
import argparse
import requests
from pprint import pprint
import time

import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Let`s say Bismillah')
parser.add_argument('-t', help='Target web/ page')
parser.add_argument('-s', help='Showing target [short name]')
parser.add_argument('-e', help='Execute/ Start crawling')
args = parser.parse_args()

wt = [' https://www.jobstreet.co.id ','https://www.infolokerlampung.net','https://www.loker.id','https://www.karir.com','https://www.urbanhire.com']
start_time = time.time()
end_time = time.time()


def tm(tm):
    end = '\n----- {} s-----\n'.format(tm*1000)
    print(end)

def target():
    src = args.t
    print(src)
    return src


def showT(a):
    if a == 'all' :
        for i in wt :
            print('\n\t Target : ',i)

    tm(start_time-end_time)

def execute(a):
    start(a)

def main():
    if args.t :
        target()
    if args.s :
        showT(args.s)
    if args.e:
        if len(args.e) > 1 :
            execute(args.e)
    else :
        pass



def start(t):
    url = t
    # url = "http://journal.portalgaruda.org/index.php/EEI/issue/archive"
    r = requests.get(url,verify=False)
    soup = BeautifulSoup(r.content,  "html.parser")
    data = soup.find("div", {"id": "opportunities_popular"})
    print(soup)


if __name__ == '__main__':
    main()


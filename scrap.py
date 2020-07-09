#!/usr/bin/python
from function import _serial
from database import *
import argparse
import requests
from pprint import pprint
import time

import requests
from bs4 import BeautifulSoup
import random
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

def test():
    url = 'https://httpbin.org/headers'
    for i in range(1,4):
        #Pick a random user agent
        user_agent = random.choice(user_agent_list)
        #Set the headers 
        headers = {'User-Agent': user_agent}
        #Make the request
        response = requests.get(url,headers=headers)
        
        print("Request #%d\nUser-Agent Sent:%s\n\nHeaders Recevied by HTTPBin:"%(i,user_agent))
        print(response.json())
        print("-------------------")




parser = argparse.ArgumentParser(description='Let`s say Bismillah')
parser.add_argument('-t', help='Target web/ page')
parser.add_argument('-s', help='Showing target [short name]')
parser.add_argument('-e', help='Execute/ Start crawling')
args = parser.parse_args()

wt = ['https://www.jobstreet.co.id/id/job-search/job-vacancy.php?ojs=10&key=it']
#wt = [' https://www.jobstreet.co.id ' ,'https://www.infolokerlampung.net' ,'https://www.loker.id' ,'https://www.karir.com' ,'https://www.urbanhire.com'] 

end = '\n---------------end\n'

def target():
    src = args.t
    print(src)
    return src


def showT(a):
    if a == 'all' :
        for i in wt :
            print('\n\t Target : ',i)
        print(end)


def execute(a):
    #sub_infolokerlampung(a)
    loker_id(a)

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

def jobstreet():
    url= "https://www.jobstreet.co.id/id/job-search/job-vacancy.php?ojs=10&key=IT"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url,headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    position = soup.find_all("h2")
    company = soup.find_all("h3",class_='company-name')
    requirement = soup.find_all("ul",class_="list-unstyled hidden-xs")
    link = soup.find_all("a",class_="position-title-link")
    salary = '-'
    progress = [ ".","..","...","....","....." ]
    for x, y,z,l in zip(position,company,requirement,link):
        id = _serial()
        data = {
            "position":x.text,
            "company": y.text,
            "salary" :salary,
            "requirement": z.text,
        
            "link":l.get("href")
        }
        time.sleep(1)
        print(random.choice(progress))
        print(data)
        db.reference("jobstreet").child(id).update(data)
        

jobstreet()


def info_loker():
    url= "https://www.infolokerlampung.net/search?q=IT"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url,headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    data = soup.find_all("h2",class_='post-title entry-title')
    for i in data:
        link = i.find('a').get('href')
        com = i.find('a').text
        print(com)
        print(link)
        x = requests.get(link,headers=headers, verify=True)
        y = BeautifulSoup(x.content,  "html.parser")
        lok = y.find_all("b")
        print(lok)
        print()
#info_loker()
        

def loker_id():
    url= "https://www.loker.id/cari-lowongan-kerja?q=it&lokasi=0"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url,headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    data = soup.find_all("div",class_='job-box')
    for i in data:
        link = i.find('h3',class_="media-heading")
        print(link.find('a').text)
        print('href :',link.find('a').get('href'))
        href= link.find('a').get('href')
        z = requests.get(href,headers=headers, verify=True)
        r = BeautifulSoup(z.content,  "html.parser")
        d= r.find_all('div',class_='panel-body padding-horizontal-double padding-vertical-double')
        print(d)
        print()
        print()
        print()
        print()
        

#loker_id()



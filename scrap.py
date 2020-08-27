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
    for i in range(1, 4):
        # Pick a random user agent
        user_agent = random.choice(user_agent_list)
        # Set the headers
        headers = {'User-Agent': user_agent}
        # Make the request
        response = requests.get(url, headers=headers)

        print("Request #%d\nUser-Agent Sent:%s\n\nHeaders Recevied by HTTPBin:" %
              (i, user_agent))
        print(response.json())
        print("-------------------")


parser = argparse.ArgumentParser(description='Let`s say Bismillah')
parser.add_argument('-t', help='Target web/ page')
parser.add_argument('-s', help='Showing target [short name]')
parser.add_argument('-e', help='Execute/ Start crawling')
args = parser.parse_args()

wt = ['https://www.jobstreet.co.id/id/job-search/job-vacancy.php?ojs=10&key=it']
#wt = [' https://www.jobstreet.co.id ' ,'https://www.infolokerlampung.net' ,'https://www.loker.id' ,'https://www.karir.com' ,'https://www.urbanhire.com','https://www.topkarir.com/lowongan?search_joblist=IT&adv_inter=&adv_lokasi=&adv_pendidikan=&group=0&adv_posisi=&adv_gaji=&adv_gaji_max=0&adv_industri=0']

# https://www.jobstreet.co.id
# https://www.jooble.com
# https://www.loker.id
# https://www.karir.com'
# https://www.topkarir.co
end = '\n---------------end\n'


def target():
    src = args.t
    print(src)
    return src


def showT(a):
    if a == 'all':
        for i in wt:
            print('\n\t Target : ', i)
        print(end)


def execute(a):
    # sub_infolokerlampung(a)
    loker_id(a)


def main():
    if args.t:
        target()
    if args.s:
        showT(args.s)
    if args.e:
        if len(args.e) > 1:
            execute(args.e)
    else:
        pass


def jobstreet():
    url = "https://www.jobstreet.co.id/id/job-search/job-vacancy.php?ojs=10&key=IT"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    position = soup.find_all("h2")
    company = soup.find_all("h3", class_='company-name')
    requirement = soup.find_all("ul", class_="list-unstyled hidden-xs")
    link = soup.find_all("a", class_="position-title-link")
    salary = '-'
    progress = [".", "..", "...", "....", "....."]
    for x, y, z, l in zip(position, company, requirement, link):
        id = _serial()
        data = {
            "id": id,
            "position": x.text.strip(),
            "company": y.text.strip(),
            "salary": salary,
            "requirement": z.text,
            "link": l.get("href")
        }
        time.sleep(1)
        print(random.choice(progress))
        db.reference("jobstreet").child(id).update(data)


#jobstreet()


def loker_id():
    url = "https://www.loker.id/cari-lowongan-kerja?q=IT&lokasi=0"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    data = soup.find_all("div", class_='job-box')
    position = soup.find_all("h3", class_="media-heading h4")
    company = soup.find_all("table", class_='table')
    salary = '-'
    progress = [".", "..", "...", "....", "....."]

    for w, x in zip(position, company):
        l = w.find('a')
        id = _serial()
        data = {
            "id": id,
            "position": w.text.strip(),
            "company": x.text.strip(),
            "salary": salary,
            "requirement": x.text,
            "link": l.get("href")
        }
        time.sleep(1)
        print(random.choice(progress))
        db.reference("lokerid").child(id).update(data)


#loker_id()


def karir():
    url = "https://www.karir.com/search"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    position = soup.find_all(
        "h4", class_='tdd-function-name --semi-bold --inherit')
    company = soup.find_all("div", class_='tdd-company-name h8 --semi-bold')
    requirement = soup.find_all("span", class_="tdd-experience")
    salary = soup.find_all("span", class_="tdd-salary")
    link = soup.find_all("a", class_="btn --full")
    progress = [".", "..", "...", "....", "....."]
    for x, y, z, l, s in zip(position, company, requirement, link, salary):
        id = _serial()
        data = {
            "id": id,
            "position": x.text.strip(),
            "company": y.text.strip(),
            "salary": s.text,
            "requirement": 'Pengalaman : ' + z.text,
            "link": 'https://www.karir.com'+l.get("href")
        }
        time.sleep(1)
        print(random.choice(progress))
        print()
        pprint(data)
        db.reference("karir").child(id).update(data)


#karir()


def topkarir():
    url = "https://www.topkarir.com/lowongan?search_joblist=IT&adv_inter=&adv_lokasi=&adv_pendidikan=&group=0&adv_posisi=&adv_gaji=&adv_gaji_max=0&adv_industri=0"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    #data = soup.find_all("div",class_='caption')
    position = soup.find_all("h3", class_='job-title')
    company = soup.find_all("h2", class_='company-title title')
    requirement = soup.find_all("div", class_="keterangan")
    #salary = soup.find_all("span",class_="")
    link = soup.find_all("a", class_="btn-small lightblue track_alto")
    progress = [".", "..", "...", "....", "....."]
    for x, y, z, l in zip(position, company, requirement, link):
        id = _serial()
        data = {
            "id": id,
            "position": x.text.strip(),
            "company": y.text.strip(),
            "salary": '-',
            "requirement": z.text,
            "link": l.get("data-url")
        }
        time.sleep(1)
        print(random.choice(progress))
        print()
        print(data)
        db.reference("topkarir").child(id).update(data)


#topkarir()


def jooble():
    url = "https://id.jooble.org/m/lowongan-kerja-IT"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    #data = soup.find_all("div",class_='caption')
    position = soup.find_all("h2", class_='_1e859')
    company = soup.find_all("span", class_='caption _8d375')
    requirement = soup.find_all("div", class_="_0b1c1")
    salary = soup.find_all("p", class_="_6f85c")
    link = soup.find_all("a", class_="baa11")
    progress = [".", "..", "...", "....", "....."]
    for x, y, z, l, s in zip(position, company, requirement, link, salary):
        id = _serial()
        data = {
            "id": id,
            "position": x.text.strip(),
            "company": y.text.strip(),
            "salary": s.text,
            "requirement": z.text,
            "link": "https://id.jooble.org"+l.get("href")
        }
        time.sleep(1)
        print(random.choice(progress))
        print()
        print(data)
        #db.reference("jooble").child(id).update(data)
jooble()

#jooble()
def JLP():
    url = "https://id.jooble.org/lowongan-kerja-it/bandar-lampung"
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers, verify=True)
    soup = BeautifulSoup(r.content,  "html.parser")
    #data = soup.find_all("div",class_='result')
    h2 = soup.find_all("h2",class_='position')
    for i in h2 :
        res = h2.find('span')
        pprint(res)



    #position = soup.find_all("h2", class_='_1e859')
    #company = soup.find_all("span", class_='caption _8d375')
    #requirement = soup.find_all("div", class_="_0b1c1")
    #salary = soup.find_all("p", class_="_6f85c")
    #link = soup.find_all("a", class_="baa11")
    progress = [".", "..", "...", "....", "....."]


#JLP()
if __name__ == "__main__":
    pass

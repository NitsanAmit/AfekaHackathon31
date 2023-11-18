import requests
from bs4 import BeautifulSoup
import re
import sys
import csv
import time

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        words = re.findall(r'\(\@([a-zA-Z0-9.\-,\~!@#$%^&*()]+)\)', soup.get_text()) #  (@NAME)
        return words
    else:
        return None
    

def get_name(raw_name):
     if not isinstance(raw_name, list):
          return None
     if len(raw_name) < 1:
          return None
     return requests.utils.requote_uri(raw_name[0])

def main():
    # if len(sys.argv) < 2:
        # return
    # csv_path = sys.argv[1]
    csv_path = "../Downloads/names.csv"
    names = []
    with open(csv_path, newline='') as csvfile:
            names = list(csv.reader(csvfile))
    names = list(map(get_name, names))
    handles = []
    for name in names:
        time.sleep(5) # to prevent getting our ip blocked
        possibleUserHandle = fetch_page("https://google.com/search?q=" + name + "%20site:twitter.com")
        if len(possibleUserHandle) > 0:
            handles.append(possibleUserHandle[0])
            print(handles)
        # Write to csv? Write to DB?
    print(handles)

main()
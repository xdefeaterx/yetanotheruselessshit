import sys
import urllib.request
import json
from pprint import pprint
from bs4 import BeautifulSoup
import gui

print (sys.version)
urllib.request.urlretrieve("http://2ch.hk/hw/res/1587296.json", "test.json")

#f = open('output.txt', 'w')

with open('test.json') as data_file:
    data = json.load(data_file)
    for i in range(0,len(data['threads'][0]['posts'])):
        soup = BeautifulSoup(data['threads'][0]['posts'][i]['comment'])
        #pprint(soup.html.get_text(), f)
        gui.insert_in_listbox(soup.html.get_text())

#f.close()
gui.on_finish()

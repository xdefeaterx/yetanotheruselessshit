import sys
import urllib.request
import json
from pprint import pprint
from bs4 import BeautifulSoup
import gui
import pickle
import constants

print (sys.version)
urllib.request.urlretrieve("http://2ch.hk/hw/res/1587296.json", "test.json")

pickledata = {}
parse_data = {constants.COMMENT:[], constants.NAME:[],
    constants.EMAIL:[], constants.NUM:[],
    constants.NUMBER:[], constants.OP:[],
    constants.PARENT:[]}

f = open('output.txt', 'w')

with open('test.json') as data_file:
    data = json.load(data_file)
    #for i in range(0,len(data['threads'][0]['posts'])):
    for i in range(0,10):
        #soup = BeautifulSoup(data['threads'][0]['posts'][i]['comment'], "lxml")
        parse_data[constants.COMMENT].append(str(data['threads'][0]['posts'][i][constants.COMMENT]))
        parse_data[constants.NAME].append(str(data['threads'][0]['posts'][i][constants.NAME]))
        parse_data[constants.EMAIL].append(str(data['threads'][0]['posts'][i][constants.EMAIL]))
        parse_data[constants.NUM].append(str(data['threads'][0]['posts'][i][constants.NUM]))
        parse_data[constants.NUMBER].append(str(data['threads'][0]['posts'][i][constants.NUMBER]))
        parse_data[constants.OP].append(str(data['threads'][0]['posts'][i][constants.OP]))
        parse_data[constants.PARENT].append(str(data['threads'][0]['posts'][i][constants.PARENT]))
        #gui.insert_in_listbox(soup.html.get_text())

pickledata[constants.COMMENT] = parse_data[constants.COMMENT]
pickledata[constants.NAME] = parse_data[constants.NAME]
pickledata[constants.EMAIL] = parse_data[constants.EMAIL]
pickledata[constants.NUM] = parse_data[constants.NUM]
pickledata[constants.NUMBER] = parse_data[constants.NUMBER]
pickledata[constants.OP] = parse_data[constants.OP]
pickledata[constants.PARENT] = parse_data[constants.PARENT]

with open('data.pickle', 'wb') as p:
        pickle.dump(pickledata, p)


with open('data.pickle', 'rb') as p:
     data_new = pickle.load(p)

#pprint(data_new[constants.PARENT], f)

f.close()

#gui.on_finish()

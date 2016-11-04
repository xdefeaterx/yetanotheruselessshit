import sys
import urllib.request
import json
from pprint import pprint
from bs4 import BeautifulSoup
import gui
import pickle
import constants
import nlp_tagger

###########__ESTABLISH INTERNET CONNECTION__##############
##########################################################

page_to_parse = "http://2ch.hk/hw/res/1587296.json"
file_to_save = "test.json"

def download(link, filo):
    try:
        urllib.request.urlretrieve(link, filo)
    except urllib.error.HTTPError:
        sys.exit("Error 404: Site can’t be reached")
    except urllib.error.URLError:
        sys.exit("Error: No Internet connection")

download(page_to_parse, file_to_save)

print("Successfully downloaded data from " + page_to_parse + " to " + file_to_save)

##########################################################

pickledata = {}
parse_data = {constants.COMMENT:[], constants.NAME:[],
    constants.EMAIL:[], constants.NUM:[],
    constants.NUMBER:[], constants.OP:[],
    constants.PARENT:[], constants.TAG:[]}

posts_amount = 10

def start_parse_data():
    with open(file_to_save) as data_file:
        data = json.load(data_file)
        #posts_amount = len(data['threads'][0]['posts'])
        for i in range(0, posts_amount):
            parse_data[constants.COMMENT].append(str(data['threads'][0]['posts'][i][constants.COMMENT]))
            parse_data[constants.NAME].append(str(data['threads'][0]['posts'][i][constants.NAME]))
            parse_data[constants.EMAIL].append(str(data['threads'][0]['posts'][i][constants.EMAIL]))
            parse_data[constants.NUM].append(str(data['threads'][0]['posts'][i][constants.NUM]))
            parse_data[constants.NUMBER].append(str(data['threads'][0]['posts'][i][constants.NUMBER]))
            parse_data[constants.OP].append(str(data['threads'][0]['posts'][i][constants.OP]))
            parse_data[constants.PARENT].append(str(data['threads'][0]['posts'][i][constants.PARENT]))
            parse_data[constants.TAG].append(nlp_tagger.set_tag(str(data['threads'][0]['posts'][i][constants.COMMENT])))

start_parse_data()
print("Data successfully parsed")

#########################################################

pickle_datafile = "data.pickle"

def make_data_to_dump():
    pickledata[constants.COMMENT] = parse_data[constants.COMMENT]
    pickledata[constants.NAME] = parse_data[constants.NAME]
    pickledata[constants.EMAIL] = parse_data[constants.EMAIL]
    pickledata[constants.NUM] = parse_data[constants.NUM]
    pickledata[constants.NUMBER] = parse_data[constants.NUMBER]
    pickledata[constants.OP] = parse_data[constants.OP]
    pickledata[constants.PARENT] = parse_data[constants.PARENT]
    pickledata[constants.TAG] = parse_data[constants.TAG]

def dump_data():
    with open('data.pickle', 'wb') as p:
            pickle.dump(pickledata, p)

make_data_to_dump()
dump_data()

print("Data successfully reorganized and dumped")

with open('data.pickle', 'rb') as p:
     data_new = pickle.load(p)

pprint(data_new[constants.TAG])

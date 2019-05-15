from bs4 import BeautifulSoup
import pandas as pd
import os 

def parse(xml):
    print("START")
    soup = BeautifulSoup(xml,'lxml')
    # location = [loc.string for loc in soup.find_all('location')]
    location_data = soup.find_all('location')

    stationid = [int(ids.string) for ids in soup.find_all('stationid')]

    ele_name = [ele.string for ele in soup.find_all('elementname')]

    values = []
    for item in soup.find_all('location'):
        ele_value = [float(ele.string) for ele in soup.find_all('value')]
        values.append(ele_value)
        print("ele values length: ", len(ele_value))
    print("value length: ", len(values))
    


def main():
    dirs = 'xml_weather/'
    filelist = os.listdir(dirs)
    for file in filelist:
        with open(dirs + file, 'r') as f:
            xml = f.read()
        parse(xml)

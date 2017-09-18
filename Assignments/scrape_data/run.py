#Program 1: Scrape Data
#Name: Karan Madishetty

import bs4 as bs
import requests
from bs4 import BeautifulSoup
import re
import itertools
import json

repo=[]
desc=[]
forked_repo=[]
for i in range(1,5):
    html="https://github.com/rugbyprof?page="+str(i)+"&tab=repositories"
    sauce=requests.get(html)
    soup = bs.BeautifulSoup(sauce.content,"html.parser")
    mylist=[]
    source=soup.findAll("li",{"class":"col-12 d-block width-full py-4 border-bottom public source"}) #finds all classes with li element
    fork=soup.findAll("li",{"class":"col-12 d-block width-full py-4 border-bottom public fork"})
    for source1 in source:
        for litag in source1.find_all("div",{"class":"d-inline-block mb-1"}):
            repo.append(litag.text.strip())
        for litag in source1.find_all("p",{"class":"col-9 d-inline-block text-gray mb-2 pr-4"}):
            desc.append(litag.text.strip())        
    for f in fork:
        for each in f("div",{"class":"d-inline-block mb-1"}):
            forked_repo.append(each.text.replace("\n"," ").replace(" ",""))
for i in range(0,len(forked_repo)):
    string=forked_repo[i]
    string = re.sub('\s+', ' ', string)
    string=string.split("Forked")
    repo.append(string[0])
    desc.append("Forked"+string[1])
new_dict = dict(zip(repo, desc))
with open('output.json', 'w+') as outfile:
        jsonData = json.dumps(new_dict,indent=True)
        outfile.write(jsonData)
outfile.close()

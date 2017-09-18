#Program 1: Scrape Data
#Name: Karan Madishetty

import bs4 as bs
import requests
from bs4 import BeautifulSoup

output=open("repositories.csv","w")
columns="Repository_Name,Description\n"
output.write(columns)
for i in range(1,5):
    html="https://github.com/rugbyprof?page="+str(i)+"&tab=repositories"
    sauce=requests.get(html)
    soup = bs.BeautifulSoup(sauce.content,"html.parser")
    c=soup.findAll("li",{"class":"col-12 d-block width-full py-4 border-bottom public source"}) #finds all classes with li elment
    # print(len(c))
    for container in c:
        r=container.findAll("h3")   #finds h3 tag and stores in h
        if(len(r)>0):
            repo=r[0].text.strip()  #text gives plain text and strip() emoves spaces and \n
        d=container.findAll("p",{"class":"col-9 d-inline-block text-gray mb-2 pr-4"})
        if(len(d)>0):
            desc=d[0].text.strip()
        output.write(repo+","+desc+"\n")
output.close()


  

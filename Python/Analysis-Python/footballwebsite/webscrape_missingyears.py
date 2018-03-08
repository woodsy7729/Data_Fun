import urllib2
from bs4 import BeautifulSoup
import csv
url1="https://www.sportsmole.co.uk/football/premier-league/2015-16/table.html"
url2="http://www.skysports.com/premier-league-table/2016"
fir="2015/16"
sec="2016/17"
page= urllib2.urlopen(url1)
soup=BeautifulSoup(page, "html.parser")
#print(soup)
table= soup.find_all("div", id="large_table")
rows=table.find_all("tr")

for thing in rows:
    print(thing)

#print(rows)
#for row in soup.find_all("tr"):
    #print(row) #tr, class = "imso-loa"

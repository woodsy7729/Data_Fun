import urllib2
from bs4 import BeautifulSoup
import csv
url="http://footballdatabase.com/ranking/world/1"
page= urllib2.urlopen(url)
soup=BeautifulSoup(page, "html.parser")
data=[]
counter=0
body = soup.find("tbody")
rows = body.find_all("tr")
for thing in rows:
    try:
        #rank=thing.find("td", class_="rank").get_text()
        club_country=thing.find("td", class_="club").a.get("title")
        cc_arr=club_country.split("(")
        club=cc_arr[0]
        country=cc_arr[1][:-1]
        points_arr=thing.find_all("td", class_="rank")
        points= (points_arr[1].get_text())
        rank=(points_arr[0].get_text())
        past_year_change_arr=thing.find_all("td", class_="club")
        for thing in past_year_change_arr:
            if "text-left" not in thing["class"]:
                past_year_change=(thing.get_text()[:-4])
                direction =thing.i.get("class")[2].split("-")[2]
                if direction == "down":
                    past_year_change+="n"
        toadd=[club,rank, country,points, past_year_change]
        data.append(toadd)
    except AttributeError:
        buf=0
#print(data)
'''
Resets data
fp = open("team_rankings.csv", "w")
fp.write("Club, Rank, Country, Points, Change from Last year\n")
fp.close()
'''
fp = open("team_rankings.csv", "a")
for line in data:
    to_write=(line[0].strip().encode("utf-8") + ", "+ line[1].encode("utf-8") + ", " + line[2].encode("utf-8") + ", " + line[3].encode("utf-8")+ ", " + line[4].encode("utf-8")+"\n")
    fp.write(to_write)
fp.close()
'''
for row in soup.find_all("tr"):
    toadd=[]
    #print(row)
    rank = row.find_all("td", class_="rank")
    club =row.find_all("td", class_="club")
    for thing in club:
        try:
            toadd.append(thing.a.get_text())
        except AttributeError:
            counter+=1
    for thing in rank:
        toadd.append(thing.get_text())
    data.append(toadd)
    toadd=[]


#now try with pandas - fix up
'''

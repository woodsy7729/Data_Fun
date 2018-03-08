from bs4 import BeautifulSoup
import requests
import re


current_url="http://www.cricbuzz.com/live-cricket-scorecard/17688/aus-vs-eng-1st-test-the-ashes-2017-18"
content = requests.get(current_url)
data = content.text
soup = BeautifulSoup(data, "html.parser")
to_regex = soup.find("div", id="page-wrapper").script.get_text()
game_id_regex = re.compile(r' \"\d*\"?')
game_regex_group = game_id_regex.search(to_regex)
game_id = game_regex_group.group()[2:-1]

url= "http://www.cricbuzz.com/api/html/cricket-scorecard/" + game_id
content = requests.get(url)
data = content.text
soup = BeautifulSoup(data, "html.parser")
whole_data= soup.find_all("div", id=re.compile("innings_."))
for thing in whole_data:
    innings = thing.find("div", class_="cb-col cb-col-100 cb-scrd-hdr-rw").span.get_text()
    sub_data= thing.find_all("div", class_="cb-col cb-col-100 cb-scrd-itms")
    #for batter in sub_data:
    bat_num=0
    while bat_num <11:
        try:
            batter_data=sub_data[bat_num].find_all("div")
            #batter_data=batter.find_all("div")
            batter_name=batter_data[0].get_text()
            dismissal = batter_data[1].span.get_text()
            if batter_data[1].label is not None:
                runs= batter_data[6].get_text()
                balls = batter_data[7].get_text()
                fours = batter_data[8].get_text()
                sixes= batter_data[9].get_text()
            else:
                runs = batter_data[2].get_text()
                balls = batter_data[3].get_text()
                fours = batter_data[4].get_text()
                sixes= batter_data[5].get_text()
            print(innings+"    "+batter_name+"    "+dismissal+"    "+runs+"    "+balls+"    "+fours+"    "+sixes)
            bat_num+=1
        except AttributeError as e:
            break

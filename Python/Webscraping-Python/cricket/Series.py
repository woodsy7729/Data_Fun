from bs4 import BeautifulSoup
import requests
import re

class Series:
    def __init__(self, link):
        #url = "http://www.cricbuzz.com/cricket-series/2538/the-ashes-2017-18/matches"
        content = requests.get(link)
        data = content.text
        soup = BeautifulSoup(data, "html.parser")
        self.__base_url= "http://www.cricbuzz.com"
        self.__table=soup.find("div", class_="cb-bg-white cb-col-100 cb-col cb-hm-rght")
        self.scrape(link)

    def scrape(self,link):
        self.first_game()
        self.next_game()

    def first_game(self):
        self.game_scrape("cb-col-100 cb-col ")

    def next_game(self):
        self.game_scrape("cb-col-100 cb-col cb-series-brdr ")

    def game_scrape(self, class_id):
        firstgames=self.__table.find_all("div", class_=class_id) #or class = "cb-col-100 cb-col cb-series-brdr "
        for thing in firstgames:
            dates=thing.find_all("span")
            #NEED YEAR DATE
            start_date= dates[0].get_text()
            end_date= dates[1].get_text()
            data=thing.find("div", class_="cb-col-75 cb-col").div
            game = data.a.span.get_text()
            venue = data.div.get_text()
            result=data.find("a", class_="cb-text-link").get_text()
            link = self.__base_url+data.find("a", class_="cb-text-link").get("href")
            content = requests.get(link)
            data = content.text
            newsoup = BeautifulSoup(data, "html.parser")
            scorelink= self.__base_url+newsoup.find("a", class_="cb-nav-tab ").get("href")

            player_of_match = newsoup.find("div", class_="cb-col cb-col-50 cb-mom-itm").find('a').get_text()
            #get new soup from scorelink
            line = game + "    " +venue+ "    " +start_date+ "    " +end_date+ "    " +result+ "    " + player_of_match
            self.batting_scorecard(scorelink, line)
            #print(line)

    def batting_scorecard(self, link, meta):
        content = requests.get(link)
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
                    print(meta + "    "+innings+"    " +"Batting"+"    "+batter_name+"    "+dismissal+"    "+runs+"    "+balls+"    "+fours+"    "+sixes)
                    bat_num+=1
                except AttributeError as e:
                    break

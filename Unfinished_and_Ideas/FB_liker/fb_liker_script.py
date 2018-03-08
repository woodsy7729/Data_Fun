import requests
import time
import getpass
import urllib2
from bs4 import BeautifulSoup
import csv
url="https://10minutemail.net/"
page= urllib2.urlopen(url)
soup=BeautifulSoup(page, "html.parser")
for row in soup.find_all("div", id="left"):
	for thing in row.find_all("div", class_="div-m-0"):
		string= str(thing)
		arr=string.split("value=")
		closer= arr[1].split("/")
		email = closer[0][1:-1]
		print(email)
		#words=arr[0].split()
		#print(words)


#div = left
#class  = div-m-0.get_text()
target_address = "http://facebook.com/r.php"
target_port = "80"
login_page = "/login"

# ----------------------

target_url = '{address}:{port}'.format(address = target_address, port = target_port)

# ----------------------------

class User(object):
	def __init__(self, login_details):
		self.cookies = None
		self.login_details = login_details

	def login(self):
		r = requests.post("{url}{page}".format(url=target_url, page=login_page), cookies=self.cookies)
		self.cookies = r.cookies

	def visit_page(self, page):
		r = requests.get("{url}{page}".format(url=target_url, page=page), cookies=self.cookies)

		r.text.split('href=')[1:]
		r.text.split('src=')[1:]

	def enter_form(self, page, form_details):
		r = requests.post("{}{}".format(url=target_url, page=page), data=form_details, cookies=self.cookies)

##def generateUsers():
	#have array of common names
	#go to the website many times.

# An example user logging in, navigating to and viewing their own page
# You should wrap this in some function and call one of these scenarios at random
# Each type of user should have a minimum of two non-trivial scenarios
# The following scenario is reasonably trivial
'''
hay_bale = User({"username":"Hay", "password":"bale"})
hay_bale.visit_page('/login')
time.sleep(3)
hay_bale.login()
time.sleep(3)
hay_bale.visit_page('/users')
time.sleep(3)
hay_bale.visit_page('/users/Hay')
'''

##go to page https://www.facebook.com/wicketkeeper.woods
#generate email. Beautiful soup to find https://10minutemail.net/
#password = strong_password
#need to see if password still works after time expired.

#profile pic: https://www.facebook.com/photo.php?fbid=841906279314006&set=a.101594303345211.4095.100004839243805&type=3&theater
#841906279314006
#https://www.facebook.com/photo.php?fbid=1741898532504143&set=a.161210677239611.38297.100000520407598&type=3&theater

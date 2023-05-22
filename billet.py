
import pushbullet

#Your Access Token from Pushbullet
api_key = "API_KEY"

#Initializing Pushbullet
pb = pushbullet.Pushbullet(api_key)


import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from bs4 import BeautifulSoup
import fake_useragent
import time
import random



#specifying the url
url = 'https://tickets.paleo.ch/content?lang=fr'

#specifying the path to the chromedriver.exe
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
#driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

def check_day(day):
	if day in driver.page_source:
		try:
			row = soup.find(text=day).parent.parent
			if "Epuisé" in row.text:
				print("Sold out")
			else:
				print("Available")
				pb.push_note(title=day, body="Available")
				#save the html file
				with open('paleo.html', 'w') as f:
					f.write(soup.prettify())
		except Exception:
			print("error")
			pb.push_note(title=day, body="error")
			#save the html file
			with open('paleo_error.html', 'w') as f:
				f.write(soup.prettify())


pb.push_note(title="START", body="Available")
while True:
	#fake user agent
	ua = fake_useragent.UserAgent()

	#opening the webpage
	try:
		driver.get(url)
	except Exception:
		print("fail")
	if driver.page_source:
		time.sleep(10)

		soup = BeautifulSoup(driver.page_source, 'html.parser')

		#save the html file
		with open('paleo.html', 'w') as f:
		 	f.write(soup.prettify())


		#seach in the paleo.html file for the text "
		check_day("Mardi 18 juillet 2023")
		check_day("Mercredi 19 juillet 2023")
		check_day("Jeudi 20 juillet 2023")
		check_day("Vendredi 21 juillet 2023")
		check_day("Samedi 22 juillet 2023")
		check_day("Dimanche 23 juillet 2023")
	
	time.sleep(random.randint(15, 30))
	#print time 
	print(time.strftime("%H:%M:%S", time.localtime()))
 

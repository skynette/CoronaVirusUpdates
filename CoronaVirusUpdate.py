import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
from time import sleep
import os
init(autoreset=True)

DSC = '''
                                +=======================================+
                                |..........COVID-19 UPDATE SCRIPT.......|
                                +---------------------------------------+
                                |#Author: L0n3W4lf                      |
                                |#Contact: cutejosh2@gmail.com          |
                                |#Date: April 2020                      |
                                |#This tool is made for educational     |
								|purposes                               |
                                |#Changing the Description of this tool |
                                |Won't made you the coder ^_^ !!!       |
                                |#Respect Coderz ^_^                    |
                                |                                       |
                                |                                       |
                                +=======================================+
                                |..........COVID-19 UPDATE SCRIPT.......|
                                +---------------------------------------+
'''

def getLink(url):
	while True:
		try:
			print("getting page")		
			page  = requests.get(url)
			break
		except Exception:
			print(Fore.RED +"[!] Error: NO/BAD INTERNET CONNECTION")
			print(Fore.GREEN+"[*] Retrying\n")
			sleep(2)
			continue
		os.system("cls")
	return page

# Initialize variables
url  = 'https://www.worldometers.info/coronavirus/'
page = getLink(url)
soup  = BeautifulSoup(page.content, 'html.parser')
links = soup.find_all('a', {"class":"mt_a"})
rows  = soup.find_all('tr')
news  = soup.find_all('li', class_="news_li")
date  = soup.find('div', class_="news_date")
datel  = soup.find_all('div', class_="news_date")
news_date = datel[0]
updates = news_date.nextSibling
dates = soup.find_all("button", class_="date-btn")
newsblock = soup.find_all('div', class_='newsdate_div')
date_index = 0
line  = ("+"+"-"*146+"+")
sn	  = 1

	
def getHeaders():
	global soup
	line  = ("+"+"-"*103+"+")
	cases = soup.find_all('div', class_='maincounter-number')
	Coronavirus_Cases, Deaths, Recovered = cases
	ccases = Coronavirus_Cases.text.strip()
	deaths = Deaths.text.strip()
	recvd  = Recovered.text.strip()
	print(Fore.LIGHTYELLOW_EX +"\t\t"+line + "\n\t\t|\tCoronavirus Cases: {0}\t\tDeaths: {1}\t\tRecovered: {2}\t\t|\n".format(ccases, deaths, recvd) + "\t\t"+line)

def update():
	global line
	global date
	print(len(line))
	print(Fore.LIGHTYELLOW_EX+line+"\n|\t\t\t\t\t\t\tLatest Updates {}\t\t\t\t\t\t\t           |\n".format(date.text)+line)

def notice():
	print(Fore.LIGHTGREEN_EX+"\n(NOTICE)\tPlease Note the default news order is in descending order, from oldest to the most recent....To cancel at anytime press CTRL-C")
	print(Fore.LIGHTGREEN_EX+"(NOTICE)\tYou can change the order by selecting 1 or 2")
	print(Fore.LIGHTGREEN_EX+"(OPTIONAL)\tYou can set the time interval between updates e.g 0.2secs, 0.5secs, 1sec e.t.c")
	print(Fore.LIGHTGREEN_EX+"(OPTIONAL)\tClick on the screen to pause feed at any time and press space to continue")
	order = """
		1. From Newest to Oldest
		2. From Oldest to Newest
			"""
	print(Fore.LIGHTGREEN_EX+""+order)

def new_updates():
	global line
	global updates
	global time_interval
	global sn
	for news in updates:
		news = news.text.split()
		while True:
			if "[source]" in news:
				news.remove("[source]")
			else:
				break
		news = " ".join(news)
		print(Style.BRIGHT+Fore.CYAN+str(sn)+"\t|"+news)
		print(Fore.BLUE+""+line)
		sleep(time_interval)
		sn+=1


getHeaders()
notice()

# Some customisations
while True:
	try:
		order_option = int(input("Order: "))
		time_interval = float(input("Time Interval: "))
		if order_option == 2:
			news  = news[::-1]
			sn = len(news)
			break
		break
	except Exception as e:
		print("Error: {}".format(e))

update()
new_updates()

# Block that rolls out the update
for april in newsblock:
	curr_date = dates[date_index].text
	print(Fore.LIGHTCYAN_EX+"\n"+line+"\n\t\t\t\t\t\t\t{}\n".format(curr_date)+line+"\n")
	curr = april
	curr_news = curr.find_all('div', class_="news_post")

	for news in curr_news:
		news = news.text.split()
		while True:
			if "[source]" in news:
				news.remove("[source]")
			else:
				break
		news = " ".join(news)
		print(Fore.LIGHTGREEN_EX+str(sn)+"\t|"+news)
		print(Fore.BLUE+""+line)
		sleep(time_interval)
		sn+=1
	date_index+=1

update()
getHeaders()
print(DSC)
import time
from selenium import webdriver
from googlefinance import getQuotes
import json


#Constants
buy_x_shares = 60000
numSharesInPort = 0




#Open webdriver
driver = webdriver.Chrome('/Users/Luke Puppo/ALScript/ALScript/ChromeDriver')  # Optional argument, if not specified will search path.
driver.get('http://www.marketwatch.com/game/');

#Allow for user to login
for x in range(0,15):
	time.sleep(1)
	print ("Time left to login: " + str(15-x))

#Opens trade window and sets nvax to trade plate
def openTradeWindow():	
	driver.get('http://www.marketwatch.com/game/wville-ap-econ/trade?view=detail&week=1&search=NVAX')
	time.sleep(1)
	driver.find_element_by_xpath("//*[@id='fakemaincontent']/section/div[2]/div/div[3]/div[2]/header/div[5]/button[2]").click()

#Gets current price from google finance
def getCurrentGooglePrice():
	json_string = json.dumps(getQuotes('NVAX'), indent=2)
	parsed_json = json.loads(json_string)
	GoogleNum = float(parsed_json[0]['LastTradePrice'])
	print(GoogleNum)
	return GoogleNum
	
	
#Gets current price from marketwatch
def getCurrentMarketWatchPrice():
	openTradeWindow()
	driver.refresh()
	MWString = driver.find_element_by_xpath("//*[@id='fakemaincontent']/section/div[2]/div/div[3]/div[2]/header/div[2]/p[1]/b/span[2]").text
	MWnum = float(MWString)
	print(MWnum)
	return MWnum
	
	
#Buys shares	
def buyShare():
	openTradeWindow()
	input = driver.find_element_by_xpath("//*[@id='trading']/div[6]/div[1]/div/div[2]/div/div/a/input")
	input.send_keys('buy_x_shares') #INSERT STOCK TO TRADE HERE
	input.submit()
	numSharesInPort = numSharesInPort + buy_x_shares
	
def sellShares():
	openTradeWindow()
	
	
def trade():
	currGooPrice = getCurrentGooglePrice()
	currMWPrice = getCurrentMarketWatchPrice()
	lastBoughtPrice = 0
	boughtShares = False
	increasePrice = False
	
	
	if currGooPrice>currMWPrice:
		buyShares()
		lastBoughtPrice = getCurrentMarketWatchPrice()
		boughtShares = True
	if lastBoughtPrice<getCurrentMarketWatchPrice() and boughtShares == True:
		sellShares()
		boughtShares = False
		
	
	
	
	

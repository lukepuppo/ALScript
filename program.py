import time
from selenium import webdriver
from googlefinance import getQuotes
import json


#Constants
shareToBuy = "NVAX"
buyXShares = 60000

#print("The current settings are: \n Share to buy: %s \n Quantity to buy: %s \n Is this correct? Y/N") % (shareToBuy,buyXShares)
#changeValues = input("Y/N  ")
#if changeValues == "N":
#	shareToBuy = input("What share would you like to buy? ")
#	buyXShares = input("How many %s shares would you like to buy? ") % (shareToBuy)

#Open webdriver
driver = webdriver.Chrome('/Users/Luke Puppo/ALScript/ALScript/ChromeDriver')  # Optional argument, if not specified will search path.
driver.get('http://www.marketwatch.com/game/');
time.sleep(1)
driver.find_element_by_xpath("//*[@id='welcome']/div[1]/button[2]").click()
time.sleep(1)

#username.send_keys('a.shayylmao@gmail.com') #USERNAME
#password = driver.find_element_by_id('password')
#password.send_keys('shekels2') #PASSWORD
#driver.find_element_by_xpath("//*[@id='submitButton']").click()
#time.sleep(1)


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
	print('Google price' +GoogleNum)
	return GoogleNum
	
	
#Gets current price from marketwatch
def getCurrentMarketWatchPrice():
	openTradeWindow()
	driver.refresh()
	MWString = driver.find_element_by_xpath("//*[@id='fakemaincontent']/section/div[2]/div/div[3]/div[2]/header/div[2]/p[1]/b/span[2]").text
	MWnum = float(MWString)
	print('MarketwatchPrice' + MWnum)
	return MWnum
	
	
#Buys shares	
def buyShare():
	openTradeWindow()
	input = driver.find_element_by_xpath("//*[@id='trading']/div[6]/div[1]/div/div[2]/div/div/a/input")
	input.send_keys(str(buyXShares)) #INSERT STOCK TO TRADE HERE
	input.submit()	
	driver.find_element_by_xpath("//*[@id='submitorder']/button").click()
	print('Bought shares')
	
def sellShares():
	openTradeWindow()
	driver.get('http://www.marketwatch.com/game/wville-ap-econ/portfolio/Holdings')
	driver.find_element_by_xpath("//*[@id='maincontent']/section[2]/div[1]/table/tbody/tr[1]/td[7]/button").click()
	driver.find_element_by_xpath("//*[@id='submitorder']/button").click()
	print('Sold shares')
	
	
	
def trade():
	openTradeWindow()
	lastBoughtPrice = 0
	boughtShares = False
	increasePrice = False
	
	while True:
		currGooPrice = getCurrentGooglePrice()
		currMWPrice = getCurrentMarketWatchPrice()
		if currGooPrice>currMWPrice:
			buyShares()
			lastBoughtPrice = currMWPrice
			boughtShares = True
		if lastBoughtPrice<currMWPrice and boughtShares == True:
			sellShares()
			boughtShares = False
			print('Price went up! Money has been made!')
		if lastBoughtPrice>currMWPrice and boughtShares == True:
			sellShares()
			boughtShares = False
			print('Price went down! Minimized losses.')
			
		time.sleep(1)
		
trade()		
	
	
	
	

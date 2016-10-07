import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from googlefinance import getQuotes
import json


#Constants
shareToBuy = "JDST"
buyXShares = 4000

changeValues = True
while changeValues == True:
	print('The current settings are: \n Share to trade: %s \n Quantity to trade: %s \n Is this correct? Y/N' % (shareToBuy,buyXShares))
	changeValues = input("Y/N  ")
	if changeValues == "N":
		shareToBuy = input("What share would you like to trade? ")
		buyXShares = input("How many %s shares would you like to trade? " % (shareToBuy))
		changeValues = False
		print('The current settings are: \n Share to trade: %s \n Quantity to trade: %s' % (shareToBuy,buyXShares))
	

driver = webdriver.Chrome('/Users/Luke/Desktop/ChromeDriver')  #/Users/Luke Puppo/AlScript/AlScript/ChromeDriver    /Users/Luke/Desktop/ChromeDriver

def startPage(driver):
	#Open webdriver
	chop = webdriver.ChromeOptions()
	chop.add_extension('extension_1_9_10.crx')
	driver = webdriver.Chrome(chrome_options = chop)


	driver.get('https://id.marketwatch.com/access/50eb2d087826a77e5d000001/latest/login_standalone.html?url=http%3A%2F%2Fwww.marketwatch.com%2Fuser%2Flogin%2Fstatus');
	username = driver.find_element_by_id("username")
	username.send_keys("a.shayylmao@gmail.com") #USERNAME
	password = driver.find_element_by_id("password")
	password.send_keys("shekels2") #PASSWORD
	driver.find_element_by_xpath("//*[@id='submitButton']").click()
	time.sleep(1)


#Opens trade window and sets WLL to trade plate
def openTradeWindow(driver):	
	driver.get('http://www.marketwatch.com/game/wville-ap-econ/trade?view=detail&week=1&search=' + shareToBuy) 
	#time.sleep(.2)
	

#Gets current price from google finance
def getCurrentGooglePrice(driver):
	json_string = json.dumps(getQuotes('%s' % (shareToBuy)), indent=2)
	parsed_json = json.loads(json_string)
	GoogleNum = float(parsed_json[0]['LastTradePrice'])
	print('Google price: ' + str(GoogleNum))
	return GoogleNum
	
	
#Gets current price from marketwatch
def getCurrentMarketWatchPrice(driver):
	openTradeWindow(driver)
	MWString = driver.find_element_by_xpath("//*[@id='fakemaincontent']/section/div[2]/div/div[3]/div[2]/header/div[2]/p[1]/b/span[2]").text
	MWnum = float(MWString)
	print('Marketwatch Price: ' + str(MWnum))
	return MWnum
	
	
#Buys shares	
def buyShares(driver):
	openTradeWindow(driver)
	driver.find_element_by_xpath("//*[@id='fakemaincontent']/section/div[2]/div/div[3]/div[2]/header/div[5]/button[2]").click()
	input = driver.find_element_by_xpath("//*[@id='trading']/div[6]/div[1]/div/div[2]/div/div/a/input")
	input.send_keys(str(buyXShares)) #INSERT STOCK TO TRADE HERE	
	driver.find_element_by_xpath("//*[@id='submitorder']/button").click()
	print('Bought shares')


def sellShares(driver):
	openTradeWindow()
	driver.get('http://www.marketwatch.com/game/wville-ap-econ/portfolio/Holdings')
	driver.find_element_by_xpath("//*[@id='maincontent']/section[2]/div[1]/table/tbody/tr/td[7]/button").click()
	time.sleep(.5)
	driver.find_element_by_xpath("//*[@id='submitorder']/button").click()
	print('Sold shares')

	
def trade(driver):
	openTradeWindow(driver)
	lastBoughtPrice = 0
	boughtShares = False
	dontBuyAnyMore = False
	runs = 0
	runner = True
	
	
	while runner == True:
		currGooPrice = getCurrentGooglePrice(driver)
		currMWPrice = getCurrentMarketWatchPrice(driver)
		if currGooPrice>currMWPrice and dontBuyAnyMore == False:
			buyShares()
			lastBoughtPrice = currMWPrice
			boughtShares = True
			dontBuyAnyMore = True
		elif lastBoughtPrice<(lastBoughtPrice+.01) and boughtShares == True:
			sellShares()
			boughtShares = False
			dontBuyAnyMore = False
			print('Price went up! Money has been made!')
		elif lastBoughtPrice>currMWPrice and boughtShares == True:
			sellShares()
			boughtShares = False
			dontBuyAnyMore = False
			print('Price went down! Minimized losses.')
		runs += runs
		if runs>100:
			runner = False
	driver.close()

		
def main():
	while True:
		startPage(driver)	
		trade(driver)
main()
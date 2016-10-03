import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/Luke/Desktop/ChromeDriver')  # Optional argument, if not specified will search path.
driver.get('http://www.marketwatch.com/game/');

for x in range(0,10):
	time.sleep(1)
	print ("Time left to login: " + str(10-x))
	
driver.get('http://www.marketwatch.com/game/wville-ap-econ/trade')

time.sleep(3)
search_box = driver.find_element_by_name('instrumentsearch ac_input unused')
time.sleep(.1)
search_box.equals(driver.switchTo().activeElement());
search_box.send_keys('NVAX') #INSERT STOCK TO TRADE HERE
search_box.submit()



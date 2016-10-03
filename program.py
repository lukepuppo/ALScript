import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/Luke Puppo/ALScript/ALScript/ChromeDriver')  # Optional argument, if not specified will search path.
driver.get('http://www.marketwatch.com/game/');

for x in range(0,15):
	time.sleep(1)
	print ("Time left to login: " + str(15-x))
	
driver.get('http://www.marketwatch.com/game/wville-ap-econ/trade?view=detail&week=1&search=NVAX')
time.sleep(1)
driver.find_element_by_xpath("//*[@id='fakemaincontent']/section/div[2]/div/div[3]/div[2]/header/div[5]/button[2]").click()



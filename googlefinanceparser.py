from googlefinance import getQuotes
import json



def getCurrentPrice():
	json_string = json.dumps(getQuotes('NVAX'), indent=2)
	parsed_json = json.loads(json_string)
	return parsed_json[0]['LastTradePrice']
	

def main():
	currentPrice = getCurrentPrice()
	float_current_price = float(currentPrice)
	print(float_current_price)

	
main()
import sys
import json
import requests
from bs4 import BeautifulSoup as bs
from Input_Parser import parse_string
from Speak import speak
from num2words import num2words

def run_stocks(input):
    if input.find('stock') != -1:
        if parse_string(input, 'stock') == '':
            query = parse_string(input, 'of')
            split = query.split()
            split.remove('stock')
            company = ' '
            company = company.join(split)
            get_stock_price(company)
        company = parse_string(input, 'of')
        return get_stock_price(company)
        

        
def get_stock_price(company):
    stock_dict = {}
    with open('company_to_ticker.json', 'r') as json_file:
        stock_dict = json.load(json_file)

    ticker = stock_dict[company]
    url = 'https://finance.yahoo.com/quote/' + ticker
    print('url = {}'.format(url))
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        print('Error, webpage status code returned {}'.format(response.status_code))
        sys.exit(1)

    html_text = response.text
    soup = bs(html_text, 'lxml')
    stock_div = soup.find('fin-streamer', class_ = 'Fw(b) Fz(36px) Mb(-4px) D(ib)')
    stock_div_text = stock_div.text
    if stock_div_text.find(',') != -1:
        stock_div_text = stock_div_text.replace(',', '')
    speak_str = num2words(stock_div_text)
    speak_str = 'the stock price of ' + company + 'is ' + speak_str
    speak(speak_str)
    return True

def main():
    get_stock_price('google')
if __name__=="__main__":
    main()


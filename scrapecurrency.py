from bs4 import BeautifulSoup
import requests

def get_curreny(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    soup.find("span", class_="ccOutputRslt")

    print(content)

get_curreny('INR', 'USD')
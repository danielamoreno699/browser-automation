import requests
from datetime import datetime
import time

# Get dynamic values from the user
ticker = input("Enter ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format: ')
to_date = input('Enter end date in yyyy/mm/dd format: ')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"}

print(f"Fetching data for ticker: {ticker}")
print(f"From Date: {from_date}")
print(f"To Date: {to_date}")

content = requests.get(url, headers=headers).content
print(content)

with open("data.csv", "wb") as file:
    file.write(content)

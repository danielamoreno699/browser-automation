import requests 


url = "https://query1.finance.yahoo.com/v7/finance/download/NFLX?period1=1666209500&period2=1697745500&interval=1d&events=history&includeAdjustedClose=true"

headers = { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"}



content = requests.get(url, headers=headers).content
#print(content)

with open("data.csv", "wb") as file:
    file.write(content)# download binary files , any type of content
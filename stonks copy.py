import requests
from bs4 import BeautifulSoup
import string
stock= int(input('how mant stocks do you want to check?'))
a=[]
for i in range(stock):
    new_symbol = [input('what stock?' )]
    
    a+=  [new_symbol.upper()]
    string.upper()
print(a)
mystocks=a

stockdata=[]



  

def getdata(symbol):

    url= 'https://finance.yahoo.com/quote/' + symbol
    r= requests.get(url)
    soup= BeautifulSoup(r.text,'html.parser')
    stock={
    'symbol':symbol,
    'price': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    'change': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    }
    return stock
    
for item in mystocks:
    stockdata.append(getdata(item))
    print('getting: ', item)

with open('prices.txt','w') as f:
    f.write(str(stockdata))

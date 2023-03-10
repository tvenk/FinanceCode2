from bs4 import BeautifulSoup
import requests

ticker = str(input("Type in all caps the ticker symbol you want to check: "))

url = "https://www.macroaxis.com/valuation/{0}".format(ticker) 

result = requests.get(url)
doc = BeautifulSoup(result.content, "html.parser")

divs = doc.find_all("div")
price = ""
for div in divs:
    if (str(div).startswith('<div class="ui large green button"')):
        div_text = str(div)
        price = div.text
        break
        

realvalue = price
print("{0} Real value: $".format(ticker),realvalue) 


url2 ="https://finance.yahoo.com/quote/{0}/".format(ticker) 


result = requests.get(url2)

doc2 = BeautifulSoup(result.text, "html.parser")

cprice = ""

tags = doc2.find_all("fin-streamer")

for tag in tags:
    if tag["data-symbol"] == ticker: 

         cprice = tag["value"]
         break

print("Current {0} price: $".format(ticker),cprice)



if float(cprice) < float(realvalue):
    print("Buy!")
else:
    print("Sell!")


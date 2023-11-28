import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://in.indeed.com/"
r = requests.get(url)
print(r)

# soup = BeautifulSoup(r.text,"lxml")

# names = soup.find("div",{"class":"_4rR01T"})
# print(names)

# for name in names:
     
#     print(name.text)

# prices = soup.find("div",{""})
# print(prices)

# for price in prices:

#     print(price.text)
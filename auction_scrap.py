import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction/2022"

r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"lxml")

table = (soup.find("table", {"class" :"ih-td-tab auction-tbl"} ))
# print(table)
headers = table.find_all("th")
# print(headers)
titles =[]
for i in headers:
     title = i.text
     titles.append(title)

     print(title)

df = pd.DataFrame(columns=titles)
print(df)

rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
print(data)
#     row = [tr.text for tr in data]
#     print(row)
#     l = len(df)
#     df.loc[l] = row

# print(df)

# df.to_csv("IPL_auction_stats_2022.csv")
ww
s
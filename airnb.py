import requests
import pandas as pd 
from bs4 import BeautifulSoup      

url = "https://www.pw.live/online-course-physics-wallah-gate-ds-and-ai/parakaram-gate-2024-data-science-ai"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text,"lxml")
details = soup.find("div",class_= "batch font-fam-medium")
# print(details.text)

teachers = soup.find_all("span",class_="font-fam-bold")
print(teachers)
print('details')
# # print(len(names))
# for name in names:
#     print(name)
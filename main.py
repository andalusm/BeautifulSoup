from bs4 import BeautifulSoup
import requests
import re

url = "https://coinmarketcap.com/"
web = requests.get(url)
doc = BeautifulSoup(web.text, "html.parser")
# print(doc.prettify())
table = doc.tbody
trs = table.contents
prices = {}
for tr in trs[:10]:
    name,price = tr.contents[2:4]
    coin_name = name.p.string
    coin_price = price.a.string
    prices[coin_name]=coin_price
for tr in trs[10:]:
    name,price = tr.contents[2:4]
    coin_name = name.find_all("span")[1].string
    coin_price = price.span.text
    prices[coin_name]=coin_price

print(prices)






# with open("index.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")
#
# # prints it very pretty
# # print(doc.prettify())
# # Finds first instance of a tag (here we find title)
# tag = doc.title
# #finds all instance of a tag
# tags = doc.find_all("a")
# # gets the string inside the tag and changes it
# tag.string = "Hello"
# print(tags)


from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"
web = requests.get(url)
doc = BeautifulSoup(web.text, "html.parser")
# print(doc.prettify())
prices = doc.find_all(text="$")
parent = prices[0].parent.find("strong")
print(parent.text)



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


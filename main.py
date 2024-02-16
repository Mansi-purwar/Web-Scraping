import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 10):
    url = "https://www.flipkart.com/search?q=phones+under+50%2C000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")

    for i in names:
        name = i.text
        Product_name.append(name)
    #print(len(Product_name))

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Prices.append(name)
    #print(len(Prices))

    desc = box.find_all("ul", class_="_1xgFaf")

    for i in desc:
        name = i.text
        Description.append(name)
    #print(len(Description))

    rev = box.find_all("div", class_="_3LWZlK")

    for i in rev:
        name = i.text
        Reviews.append(name)
    #print(len(Reviews))

df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})
#print(df)

df.to_csv("E:/python/Web Scraping/flipkart_mobiles_under50000.csv")

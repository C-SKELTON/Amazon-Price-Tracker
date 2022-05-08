from bs4 import BeautifulSoup
import requests
import lxml
from datetime import date




headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

current_date = str(date.today()).strip()
product_list = []
price_list = []
url_list = []

with open("Product_URLs.txt") as f:
    contents = f.readlines()


for product in range(len(contents)):
    product_url = contents[product]
    response = requests.get(product_url, headers=headers)

    amazon_page = response.text
    soup = BeautifulSoup(amazon_page, "lxml")
    price = soup.find("span", class_="a-offscreen").getText()
    product_title = soup.find("span", id="productTitle").getText().strip()
    price_without_currency = float(price.split("$")[1])
    price_as_string = str(price)

    product_list.append(product_title)
    price_list.append(price_as_string)
    url_list.append(product_url)
product_list_len = len(product_list)

for x in range(product_list_len):
    with open("amazon-prices.csv", "a") as file:
       file.write(f"{current_date}; ")
       file.write(f"{product_list[x]}; ")
       file.write(f"{price_list[x]}; ")
       file.write(f"{url_list[x]} ")
       file.write("\n")

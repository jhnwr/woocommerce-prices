import requests
from bs4 import BeautifulSoup

url = 'https://www.okonline.co.zw/?product_cat=grocery'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

products = soup.find_all('div', class_ = 'product-wrapper')

for product in products:
    title = product.find('div', class_ = 'product-name').text.strip()
    price = product.find('div', class_ = 'price-box-inner').text.strip()

    item = {
            'title': title,
            'price': price[:-2] + '.' + price[-2:]
           }
    print(item)

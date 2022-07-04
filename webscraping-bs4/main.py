from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.newegg.com/p/pl?N=100006740%204814%2050010418&cm_sp=Cat_Laptops-_-PopBrands-_-Lenovo_3'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

items_containers = soup.find_all(class_='item-container')
#print(items_containers)
items_data = []
headers = ['title', 'past_price', 'current_price', 'discount', 'price_shipping']

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for item in items_containers:
        item_info = soup.find(class_='item-info')
        title = item_info.find(class_='item-title').get_text()
    

        item_action = soup.find('div', class_='item-action')
        price = item_action.find(class_='price')
        past_price = price.find(class_='price-was').text
        

        current_price = price.find(class_='price-current').text
        

        discount= price.find(class_='price-save').text
        

        price_ship = price.find(class_='price-ship').text
        data = [title, past_price, current_price, discount, price_ship]
        writer.writerow(data)
        
        # items_data.append({ 'Item':{
        #     'title': title, 'past_price': past_price, 'current_price': current_price,
        #     'discount': discount, 'price_ship': price_ship }
        # })


print(items_data)

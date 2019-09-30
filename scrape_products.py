from bs4 import BeautifulSoup
import requests
from send_mail import send_mail


products = [{'name': 'Gigabyte-GeForce-RTX-2060-Super-8GB-Aorus', 'url': 'https://www.skroutz.gr/s/19396716/Gigabyte-GeForce-RTX-2060-Super-8GB-Aorus-GV-N206SAORUS-8GC.html'},
            {'name': 'AMD-Ryzen-7-2700X', 'url': 'https://www.skroutz.gr/s/14650952/AMD-Ryzen-7-2700X-Box.html'},
            {'name': 'Asus-Rog-Strix-X470-F-Gaming', 'url': 'https://www.skroutz.gr/s/14682943/Asus-Rog-Strix-X470-F-Gaming.html'},
            {'name': 'Samsung-970-Evo-Plus-500GB', 'url': 'https://www.skroutz.gr/s/17274661/Samsung-970-Evo-Plus-500GB.html'}]


for product in products:
    print(f"Processing product in: {product['url']}")

    # get content of specified url
    soup = BeautifulSoup(requests.get(product['url']).text, 'html.parser')
    # search for price
    product['price'] = soup.find('span', {'class': 'price js-price'}).text
    
send_mail(products)
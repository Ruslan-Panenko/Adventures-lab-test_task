from bs4 import BeautifulSoup
import requests
from threading import Thread

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"

result = []
id = 0


def parse(url):
    response = requests.get(url, headers=
    {"user-agent": user_agent})
    soup = BeautifulSoup(response.text, "html.parser")

    data = soup.find_all('div', class_='css-qfzx1y')
    for car in data:
        res = {}
        try:
            title = car.find('h6', class_='css-v3vynn-Text eu5v0x0')
            price = car.find('p', class_='css-wpfvmn-Text eu5v0x0')
            img = car.find(class_='css-gl6djm').find(class_='css-8wsg1m').get('src')

        except:
            pass
        global id
        res['id'] = id
        res['title'] = title.text
        res['price'] = price.text
        res['img'] = img
        global result
        result.append(res)
        id += 1


def parce():
    urls = ['https://www.olx.ua/d/uk/transport/legkovye-avtomobili/',
            'https://www.olx.ua/d/uk/transport/legkovye-avtomobili/?page=2']
    for url in urls:
        thread = Thread(target=parse, args=(url,))
        thread.start()
        thread.join()
    return result

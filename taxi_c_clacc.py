
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
#print(ua.ie) Mozila
print()

def zapros():
    headers = {'User-Agent': ua.ie}
    url = 'https://www.taxirenault.ru/auto.asp?gr=1007'    
    response = requests.get(url,headers=headers)
    return response


def foto_car(response):
    link= f'https://www.taxirenault.ru'

    soup = BeautifulSoup(response.text, 'lxml')  
    block = soup.find('div', class_="c-auto__list") 
    foto_block = block.find_all('a')

    links_all_a = [] 
    for adress in foto_block:
        if adress.get('href')[-1] == 'g':
            links_all_a.append(adress.get('href'))
           
    
    for adres in range(len(links_all_a)):
        img = requests.get(f'{link}{links_all_a[adres]}')
        with open(f'/Volumes/disk D/python/progect/parser_page/foto_parser/{adres}.jpg', "wb") as file:
            file.write(img.content)
            print("Успешно",' -> ',f'/Volumes/disk D/python/progect/parser_page/foto_parser/{adres}.jpg')  


if zapros():
    print("Соединение установлено: ",zapros())
    foto_car(zapros())
else:
    print('Проблемы с соединением!')    
print()

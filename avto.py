
from numpy import block
import requests
from bs4 import BeautifulSoup
from faker import Faker
import json

print()
def zapros():
    """Проверяет доступность для работы сраницы и выводит  responce"""
    link = 'https://auto.ru/voronezh/cars/toyota/all/?year_from=1991&year_to=2003&steering_wheel=RIGHT&price_to=280000'
    header = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.74"}
    sait = requests.get(link, headers=header)
    #print(sait) #200 responce
    #print(type(sait))
    return sait

   

def parsing():
    sait = zapros()   
    responce = sait.content.decode('utf-8') # decoding artefacts
    soup = BeautifulSoup(responce, 'html.parser')
    blocks = soup.find_all('script') #all bloks on my page

    #find toyota VII , информация находится внутри скрипта, а не внутри открытого тега! 
    toyota = blocks[1].text     #type-str мы взяли первое объявление и работаем с ним
    index = 0
    for car in blocks[1:29]:
        index+=1
        print('Index on list blocks: ',index)
        car = car.text
        my_list=[] 
        for i in car.split(','):
            my_list.append(i) #create list value
        car_information = []
        for i in my_list:
            car_information.append(i)
        print(car_information[2],car_information[4],car_information[7],car_information[12],car_information[13], sep='\n')
        print()
    
    
   
    print()

    # преобразовать строку в словарь для извлечения информации по ключю

    
if str(zapros()) == '<Response [200]>' :
    print('Соединение установленo')
    print()
    parsing()


#print(help(requests))
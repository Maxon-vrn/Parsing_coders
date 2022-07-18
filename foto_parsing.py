import requests
from bs4 import BeautifulSoup

print()

def connect():
    """Проверка соединения с сайтом """
    storage_number = 1     #page number on sait
    link = f"https://zastavok.net"
    sait = requests.get(f'{link}/{storage_number}') #запрос на первую - главную страницу сайта!
    return sait

def parsing(sait):
    """Если все удачно, начинаем разбирать страницу"""
    image_number = 0
    storage_number = 1     #page number on sait
    link = f"https://zastavok.net"

    soup = BeautifulSoup(sait.text,'lxml')  #.text форматироуем старницу в полноценный ответ текстом | lxml - parser
    block = soup.find('div', class_="block-photo") #находим основной блок где все лежит
    all_image = block.find_all('div',class_="short_full") #this is type-list

    
    for image in all_image:
        image_link = image.find('a').get('href')    #.get('href') - достает значение тега!!! получаем ссылку на страницу для скачки
        download_storage= requests.get(f'{link}{image_link}').text     #мы на странице для скачки картинк(страница открывается при нажатии)
        download_soup = BeautifulSoup(download_storage, 'lxml')
        download_blok = download_soup.find('div',class_="image_data" ).find('div',class_="block_down")
        #print(download_blok) find and go all pages where live link to download
        result_link = download_blok.find('a').get('href')

        """Скачивание изображений """
        image_bytes = requests.get(f'{link}{result_link}').content #content foto
        with open(f'foto_parser/{image_number}.jpeg','wb') as file: 
            file.write(image_bytes)    #запись полученных байтов/картинок

        print(f'Изображение {image_number}.jpeg скачано успешно')
        image_number +=1    #изменение номера скачанной картинки

            



if connect():
    print('Соединение установлено: ',connect())
    print()
    parsing(connect())
    print()
else:
    print('Ошибка соединения: ',connect())

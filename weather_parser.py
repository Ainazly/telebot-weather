import requests
from bs4 import BeautifulSoup as BS



def get_response(url):
    response = requests.get(url)
    return response.text


my_url = get_response('https://sinoptik.ua/')


def get_info(html):
    object_1 = BS(html, 'html.parser')
    days = object_1.find('div', {'class': 'tabs'})
    pogoda = days.find('div', {'id': 'bd1'}).text.split()
    temp_today = object_1.find('div', {'class': 'tabsContent'})
    temp_now = temp_today.find('p', {'class':'today-temp'}).text
    text_ = temp_today.find('div', {'class': 'description'}).text.lstrip()
    f1 = ''
    for i in pogoda[0:3]:
        f1 += str(i) + " "
    f2 = ''
    for i in pogoda[3::]:
        f2 += str(i) + " "
    return f'{f1}\n{f2}.\nТемпература сейчас: {temp_now} \n{text_}'


def get_info2(html):
    object_1 = BS(html, 'html.parser')
    days = object_1.find('div', {'class': 'tabs'})
    pogoda2 = days.find('div', {'id': 'bd2'}).text.split()
    temp_today = object_1.find('div', {'class': 'tabsContent'})
    text_ = temp_today.find('div', {'class': 'description'}).text.lstrip()
    p1 = ''
    for i in pogoda2[0:3]:
        p1 += str(i) + " "
    p2 = ''
    for i in pogoda2[3::]:
        p2 += str(i) + " "
    return f'{p1}\n{p2}\n{text_}'


get_info(my_url)
get_info2(my_url)


import csv
import os
import re

import requests
from bs4 import BeautifulSoup

# with open('shelters.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')


states_page = requests.get('https://www.domesticshelters.org/help')
bs_states_page = BeautifulSoup(states_page.text, 'html.parser')

states_divs = bs_states_page.find('div', {'class': 'column-list column-list--3x2 states-list'})
# print(states_divs)
states_list = states_divs.find('ul', {'class': 'column-list__column'}).find_all('li')
print(len(states_list))

for state in states_list:
    state_link = state.find('a')
    print(state_link)
    state_name = state_link.text
    print(state_name)
    state_href = state_link['href']
    print(state_href)

    cities_page = requests.get('https://www.domesticshelters.org' + state_href)
    bs_cities_page = BeautifulSoup(cities_page.text, 'html.parser')

    cities_div_h2 = bs_cities_page.find('h2', text=re.compile('Cities with Domestic Violence Programs$'))
    print(cities_div_h2)
    cities_div_lis = cities_div_h2.find_next_sibling().find_all('li')

    for city in cities_div_lis:
        city_a = city.find('a')
        print(city_a.text)
        print(city_a['href'])

        city_page = requests.get('https://www.domesticshelters.org' + city_a['href'])
        bs_city = BeautifulSoup(city_page.text, 'html.parser')

        city_div = bs_city.find('div', {'class': 'clearfix'}).find('h2')
        city_name = city_div.find('a')
        print(city_name.text)
        print(city_name['href'])

        city_detail = requests.get('https://www.domesticshelters.org' + city_name['href'])
        print('https://www.domesticshelters.org' + city_name['href'])
        bs_city_detail = BeautifulSoup(city_detail.text, 'html.parser')

        hotline = bs_city_detail.find('h3', text=re.compile('^Hotline$'))
        print(hotline)
        hotline_number = hotline.find_next_sibling().find('a')
        if hotline_number:
            hotline_number = hotline_number.text
            print(hotline_number)
        else:
            hotline_number = ''
        tolfree = bs_city_detail.find('h3', text=re.compile('^Toll Free$'))
        tolfree_number = tolfree.find_next_sibling().find('a')
        if tolfree_number:
            tolfree_number = tolfree_number.text
            print(tolfree_number)
        else:
            tolfree_number = ''
        business = bs_city_detail.find('h3', text=re.compile('^Business$'))
        business_number = business.find_next_sibling().find('a')
        if business_number:
            business_number = business_number.text
            print(business_number)
        else:
            business_number = ''
        text = bs_city_detail.find('h3', text=re.compile('^Text$')).find_next_sibling()
        if text:
            print(text.text)




import time

import requests
import camelot


def load_link(link):
    try:
        page = requests.get(link, timeout=10)
    except Exception as e:
        print(e.args)
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link(link)
    return page


counter = 1000
day1 = 21


def parse(count):
    global counter, day1
    print(day1, '--', counter)
    list_izb = load_link(f'https://shailoo.gov.kg/media/support3/2020/10/{day1}/{count}.pdf')

    if list_izb.status_code == 200:
        print(f'есть участок качаю {count}')
        with open(f'{count}.pdf', 'wb') as f:
            f.write(list_izb.content)





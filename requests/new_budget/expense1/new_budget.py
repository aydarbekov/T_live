import csv
import json
import os
import time
from itertools import islice

import requests
from bs4 import BeautifulSoup




# with open('new_budget_income.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerow(["ИНН", "Номер документа", "Дата платежа", "Плательщик", "Назначение платежа", "Сумма"])

# header = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,ky;q=0.6',
#     'Connection': 'keep-alive',
#     'Cookie': 'XSRF-TOKEN=eyJpdiI6Im8yME9DVzRDVkhLaUZKN0diTDhWeHc9PSIsInZhbHVlIjoiNzVrcHdsekpadTdwTGNKVmlkcVVLNnBaNGNvV2NVTjNYVW1XTlBWV09YVE5UUHlYMDRVRWNKUTl2SzVnNVJvaCIsIm1hYyI6IjQ0ODI2NGNmZjhmZmNkMjJlMWRiNzUwYzA1ZDg4ZGExODkxNTljZGE5ODIyMjZlMzAxNGRjYzU4YTBhM2E5NjUifQ%3D%3D; laravel_session=eyJpdiI6ImpkeHcvRVBheXkyTjh5bndjUFFPR1E9PSIsInZhbHVlIjoiVDZ5YTM3eWptTVFSbm9JSEZrV1N3NDJLeit3S2F0anprSEJLSS8wNmFHbEhoWHhsTDN0Nis5OGh0SE1tZnVoZiIsIm1hYyI6IjhhNDc4NDNkMmFkMmUwZTUyMmIwM2MwNWU1ZDVlYTgxYmQ2MDg4YjAyNzY3Y2Y5NjFlZGI3YTA1NWU2YzVhMGEifQ%3D%3D',
#     'Host': 'budget.okmot.kg',
#     'Referer': 'https://budget.okmot.kg/ru/expenses',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Length': '85',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'symfony=dltilhg3v3lo8au72ob7r7jsdq',
#     'dnt': '1',
#     'Host': 'oldbudget.okmot.kg',
#     'Origin': 'https://oldbudget.okmot.kg',
#     'Referer': 'https://oldbudget.okmot.kg/inn_income?code=00108199710153',
#     'Sec-Fetch-Dest': 'iframe',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
# }


data = {
    'from': '01.01.2018',
    'to': '04.12.2020',
    'submit': 'Показать',
}

# headers=header,
def load_link(link):
    try:
        page = requests.get(link, timeout=30)
    except Exception as e:
        print(e.args)
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link(link)
    return page


count = 2700

with open('../../../data/minjust.csv', 'r', newline='') as file:
    rows = csv.reader(file, delimiter='|')

    for row in islice(rows, 2701, None):
        try:
            count += 1
            print(count)

            if row[8] == 'ИНН' or row[8] == '' or row[8] == 'сведений нет':
                continue
            print(row[8])
            if len(row[8]) != 0:
                dif = 14 - len(row[8])
                inn = ('0'*dif) + row[8]
            else:
                inn = ''
            print(inn)
            inn = inn.strip()
            print(f'https://budget.okmot.kg/ru/expenses/get-inn?inn={inn}&dateFrom=2018-01-01&dateTo=2020-12-04')
            zapros = load_link(f'https://budget.okmot.kg/ru/expenses/get-inn?inn={inn}&dateFrom=2018-01-01&dateTo=2020-12-04')
            # print(list(zapros.text)[0])
            income = json.loads(zapros.text)
            print(income)
            data = income[0]
            print(type(data))
            data = json.loads(data)
            data = data['response']
            print(data)
            if isinstance(data, list):
                for item in data:
                    date_full = item['date']
                    date_new, date_sec = date_full.split('T')
                    print(inn)
                    print(item['number'])
                    # print(item['date'])
                    print(date_new)
                    print(item['payer'])
                    print(item['descr'])
                    print(item['amount'])
                    number = item['number']
                    # date = item['date']
                    payer = item['payer']
                    descr = item['descr']
                    amount = item['amount']
                    with open('new_budget_income.csv', 'a+', newline='') as file:
                        writer = csv.writer(file, delimiter='|')
                        writer.writerow([inn, number, date_new, payer,
                                         descr, amount])
            elif isinstance(data, dict):
                date_full = data['date']
                date_new, date_sec = date_full.split('T')
                print(inn)
                print(data['number'])
                # print(item['date'])
                print(date_new)
                print(data['payer'])
                print(data['descr'])
                print(data['amount'])
                number = data['number']
                # date = item['date']
                payer = data['payer']
                descr = data['descr']
                amount = data['amount']
                with open('new_budget_income.csv', 'a+', newline='') as file:
                    writer = csv.writer(file, delimiter='|')
                    writer.writerow([inn, number, date_new, payer,
                                     descr, amount])
        except Exception as e:
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
            print(e)
            print('какая то ошибка и идем дальше')
            with open('error_p.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerow(row[8])

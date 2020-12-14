import csv
import time
from itertools import islice

import requests
from bs4 import BeautifulSoup




with open('old_budget_expensed_14.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["ИНН", "Номер документа", "Дата платежа", "Плательщик", "Назначение платежа", "Сумма"])

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '85',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'symfony=dltilhg3v3lo8au72ob7r7jsdq',
    'dnt': '1',
    'Host': 'oldbudget.okmot.kg',
    'Origin': 'https://oldbudget.okmot.kg',
    'Referer': 'https://oldbudget.okmot.kg/inn_expense?code=00108199710153',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}
data = {
    'from': '06.01.2013',
    'to': '24.11.2020',
    'submit': 'Показать',
}


def load_link(link):
    try:
        page = requests.post(link, headers=header, data=data, timeout=30)
    except:
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link(link)
    return page

count = 0

with open('../../../data/minjust.csv', 'r', newline='') as file:
    rows = csv.reader(file, delimiter='|')
    for row in islice(rows, 134682, None):

        count += 1
        print(count)

        if row[8] == 'ИНН' or row[8] == '':
            continue
        print(row[8])
        if len(row[8]) != 0:
            dif = 14 - len(row[8])
            inn = ('0'*dif) + row[8]
        else:
            inn = ''
        print(inn)

        zapros = load_link(f'https://oldbudget.okmot.kg/inn_expense?code={inn}')

        bs_html = BeautifulSoup(zapros.text, 'html.parser')
        trs = bs_html.findAll('tr')
        if len(trs[1:-1]) != 0:
            for tr in trs[1:-1]:
                tds = tr.findAll('td')
                doc_num = tds[0]
                date = tds[1]
                payer = tds[2]
                dest = tds[3]['title']
                sum = tds[4]
                if payer == 'Только для юрид. лиц':
                    continue
                print(doc_num.text)
                print(date.text)
                print(payer.text)
                print(dest)
                print(sum.text)

                with open('old_budget_expensed_14.csv', 'a+', newline='') as file:
                    writer = csv.writer(file, delimiter='|')
                    writer.writerow([inn, doc_num.text, date.text, payer.text,
                                     dest, sum.text])

        bs_html.decompose()

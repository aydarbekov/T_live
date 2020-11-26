import csv

import requests
from bs4 import BeautifulSoup

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
    'Referer': 'https://oldbudget.okmot.kg/inn_income?code=00108199710153',
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


with open('../data/minjust_firms.csv', 'r', newline='') as file:
    rows = csv.reader(file, delimiter='|')
    for row in rows:
        print(row[8])

zapros = requests.post('https://oldbudget.okmot.kg/inn_income?code=00108199710153', headers=header, data=data)
print(zapros)
print(zapros.text)

bs_html = BeautifulSoup(zapros.text, 'html.parser')
trs = bs_html.findAll('tr')
# print(len(trs[1:-1]))
if len(trs[1:-1]) == 0:
    for tr in trs[1:-1]:
        print(tr)
        tds = tr.findAll('td')
        doc_num = tds[0]
        date = tds[1]
        payer = tds[2]['title']
        dest = tds[3]['title']
        sum = tds[4]
        print(payer)



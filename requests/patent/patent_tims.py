import csv
import os

import requests
from bs4 import BeautifulSoup

with open('patent_tims.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    # writer.writerow(['№', "№ регистрации", "Товарный знак", "Владелец", "№ заявки", "Дата подачи",
    #                  "Дата окончания", 'МКТУ', 'Вид знака'])

data = {
        'txt_num_svid_t': '',
        'txt_date_svid_t': '',
        'txt_number_reg_t': '',
        'txt_in_date_t': '',
        'txt_name_t': '',
        'txt_app_t': '',
        'txt_avtor_t': '',
        'txt_owner_t': '',
    }

patent_page = requests.post("http://base.patent.kg/tims.php?action=search", data=data)
bs_patent = BeautifulSoup(patent_page.text, 'html.parser')
table = bs_patent.find('table')
trs = table.find_all('tr')
counter = 0

for tr in trs[1:]:
    counter += 1
    patent = []
    print(tr)
    print(counter)
    tds = tr.find_all('td')
    print(tds)
    print(len(tds))
    number = tds[0]
    patent.append(number.text)
    num_reg = tds[1]
    patent.append(num_reg.text)
    trademark = tds[2]
    patent.append(trademark.text)
    owner = tds[3]
    patent.append(owner.text)
    request_number = tds[4]
    patent.append(request_number.text)
    date_start = tds[5]
    patent.append(date_start.text)
    date_end = tds[6]
    patent.append(date_end.text)
    mktu = tds[7]
    patent.append(mktu.text)
    sign_type = tds[8]
    patent.append(sign_type.text)
    reg_date = tds[9]
    patent.append(reg_date.text)
    # reg_date_3 = tds[10]
    # patent.append(reg_date_3.text)


    with open('patent_tims.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(patent)
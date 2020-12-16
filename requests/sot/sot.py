import csv
import os
import re

import requests
from bs4 import BeautifulSoup

with open('sot.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['Ссылка', "Название дела", "Номер дела", "Тип дела", "Состояние дела", "Статус дела", "Истец", 'Ответчик', 'Регистрация на сайте	', 'Третьи лица	', 'Судья докладчик', 'Суд', 'Адрес суда', 'Контакты суда', 'Веб сайт', 'Кол-во актов', 'Акты', 'Кол-во заседаний', 'Заседания'])

page = 1
try:
    while True:
        print(page)
        sot_page = requests.get(f'http://act.sot.kg/ru/search?caseno=&name=&articles=&court=%D0%A2%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9+%D1%80%D0%B0%D0%B9%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9+%D1%81%D1%83%D0%B4+%D0%98%D1%81%D1%81%D1%8B%D0%BA-%D0%9A%D1%83%D0%BB%D1%8C%D1%81%D0%BA%D0%BE%D0%B9+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8&judge=345&caseOpenedFrom=&caseType=all&actType=all&caseOpenedTo=&from=&to=&side1=&side2=&submit-case=%D0%94%D0%B5%D0%BB%D0%B0&page={page}')
        page += 1
        bs_sot = BeautifulSoup(sot_page.text, 'html.parser')
        trs = bs_sot.find('tbody', {'class':'tbody-data-list'}).find_all('tr')

        for tr in trs:
            tds = tr.find_all('td')
            delo_num = tds[1].find('a')

            detail = requests.get('http://act.sot.kg' + delo_num['href'])
            sot = []
            sot.append('http://act.sot.kg' + delo_num['href'])
            bs_detail = BeautifulSoup(detail.text, 'html.parser')
            tables = bs_detail.find_all('table', {'class':'table table-bordered table-striped case-table'})

            trs = tables[0].find_all('tr')
            # print(len(trs))
            delo_name = trs[0].find('td')
            sot.append(delo_name.text)
            print(delo_name.text)
            delo_num = trs[1].find('td')
            sot.append(delo_num.text)
            print(delo_num.text)
            delo_type = trs[2].find('td')
            sot.append(delo_type.text)
            print(delo_type.text)
            delo_sostoyanie = trs[3].find('td')
            sot.append(delo_sostoyanie.text)
            print(delo_sostoyanie.text)
            delo_status = trs[4].find('td')
            sot.append(delo_status.text)
            print(delo_status.text)
            istec = trs[5].find('td')
            sot.append(istec.text)
            print(istec.text)
            otvetchik = trs[6].find('td')
            sot.append(otvetchik.text)
            print(otvetchik.text)
            registr_date = trs[7].find('td')
            sot.append(registr_date.text)
            print(registr_date.text)
            try:
                third_faces = trs[8].find_all('td')[1]
                sot.append(third_faces.text)
                print(third_faces.text)
            except:
                sot.append('нету третьих лиц')
                print('нету третьих лиц')

            trs = tables[1].find_all('tr')
            # print(len(trs))
            sudya_dokladchik = trs[0].find('td')
            sot.append(sudya_dokladchik.text.strip())
            print(sudya_dokladchik.text.strip())
            sud = trs[1].find('td')
            sot.append(sud.text)
            print(sud.text)
            sud_adress = trs[2].find('td')
            sot.append(sud_adress.text)
            print(sud_adress.text)
            sud_contacts = trs[3].find('td')
            sot.append(sud_contacts.text)
            print(sud_contacts.text)
            web_site = trs[4].find('td').find('a')
            sot.append(web_site.text + ' - ' + web_site['href'])
            print(web_site.text, web_site['href'])

            trs = tables[2].find('tbody').find_all('tr')
            print(len(trs))
            sot.append(len(trs))
            if len(trs) > 0:
                act = []
                for tr in trs:
                    tds = tr.find_all('td')
                    act_name = tds[0]
                    act.append(act_name.text.strip())
                    print(act_name.text.strip())
                    file = act_name.find('a')
                    act.append('http://act.sot.kg' + file['href'])
                    print('http://act.sot.kg' + file['href'])
                    act_type = tds[1].text
                    act.append(act_type.strip())
                    print(act_type.strip())
                    acception_date = tds[2].text
                    act.append(acception_date)
                    print(acception_date)
                    publicated_to_site = tds[3].text
                    act.append(publicated_to_site)
                    print(publicated_to_site)
                sot.append(act)
            else:
                sot.append('Нету актов')

            trs = tables[3].find('tbody').find_all('tr')
            print(len(trs))
            sot.append(len(trs))
            if len(trs) > 0:
                zased = []
                for tr in trs:
                    tds = tr.find_all('td')
                    zased_time = tds[0].text
                    zased.append(zased_time)
                    print(zased_time)
                    sud = tds[1].text
                    zased.append(sud)
                    print(sud)
                    sudya_dokladchik = tds[2].text
                    zased.append(sudya_dokladchik.strip())
                    print(sudya_dokladchik.strip())
                    published_to_site = tds[3].text
                    zased.append(published_to_site)
                    print(published_to_site)
                sot.append(zased)
            else:
                sot.append('Нету заседаний')
            with open('sot.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerow(sot)
except Exception as e:
    print(e)
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))






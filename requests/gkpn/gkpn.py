import csv
import os
import time

import requests
from bs4 import BeautifulSoup


# with open('gkpn.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerow(['Номер лицензии/заявки, дата выдачи, срок действия', "Название объекта", "Недропользователь",
#                      "ИНН/ОКПО", "Местораположение объекта, область, район", "Номер и срок действия ЛС",
#                      "Вид полезного ископаемого", 'Вид недропользования', 'Полезное ископаемое',
#                      'Размер площади', 'Контактные данные недропользователя', 'ГЛФ', 'Открытый Бюджет',
#                      '№ Точки', 'Координаты X', 'Координаты Y'])

data = {
        'Filter.LicenseNumber': '',
        'Filter.AdministrativeUnit': '',
        'Filter.SquareName': '',
        'Filter.CompanyName': '',
        'Filter.Inn': '',
        'Filter.MinSize': '',
        'Filter.MaxSize': '',
        'Filter.isforest': 'false',
    }

page = 83
counter = 0


def load_link(link, data):
    try:
        page = requests.post(link, data=data, timeout=60)
        print(page.status_code)
        # print(page.text)
        if page.status_code == 500 or page.status_code == 403:
            print('ОШИБКА, пробую еще через 5 сек')
            time.sleep(5)
            page = load_link(link, data)
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
    except Exception as e:
        print(e.args)
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link(link, data)
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
    return page


def load_link_get(link):
    try:
        page = requests.get(link, timeout=60)
        # print(page.status_code)
        # print(page.text)

        if page.status_code == 500 or page.status_code == 403:
            print('ОШИБКА, пробую еще через 5 сек')
            time.sleep(5)
            page = load_link_get(link)
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
    except Exception as e:
        print(e.args)
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link_get(link)
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
    return page


while True:
    print(page, 'страница')
    gkpn_page = load_link(f"http://open.gkpen.kg/Licenses/Licenses/LicensesList?isForest=False&searching=True&isLicense=True&page={page}", data=data)
    page += 1
    bs_gkpn= BeautifulSoup(gkpn_page.text, 'html.parser')
    body = bs_gkpn.find('tbody')


    if body:
        trs = body.find_all('tr')
        if len(trs) == 0:
            page -= 1
            continue
        print(len(trs))
        for tr in trs:

            counter += 1
            print(counter)
            tds = tr.find_all('td')
            number = tds[0]
            object_name = tds[1]
            print(object_name.text)
            user = tds[2]
            inn = tds[3]
            location = tds[4]
            number_ls = tds[5]
            mineral_type = tds[6]
            use_type = tds[7]
            mineral = tds[8]
            size = tds[9]
            contacts = tds[10]
            glf = tds[11]
            open_budget = tds[12].find('a')
            coordinates = tds[13].find('a')
            if not coordinates:
                page -= 1
                counter -= 1
                os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
                break

            coordinates_pages = load_link_get("http://open.gkpen.kg" + coordinates['href'])
            # print(coordinates_pages.text)
            bs_coordinates_pages = BeautifulSoup(coordinates_pages.text, 'html.parser')
            body = bs_coordinates_pages.find('tbody')

            trs_2 = body.find_all('tr')
            for tr_2 in trs_2:
                tds = tr_2.find_all('td')
                gkpn_list = []
                gkpn_list.append(number.text)
                gkpn_list.append(object_name.text)
                gkpn_list.append(user.text)
                gkpn_list.append(inn.text)
                gkpn_list.append(location.text)
                gkpn_list.append(number_ls.text)
                gkpn_list.append(mineral_type.text)
                gkpn_list.append(use_type.text)
                gkpn_list.append(mineral.text)
                gkpn_list.append(size.text)
                gkpn_list.append(contacts.text)
                gkpn_list.append(glf.text)
                gkpn_list.append(open_budget.text + ' - ' + open_budget['href'])
                point_number = tds[2]
                gkpn_list.append(point_number.text)
                x = tds[3]
                gkpn_list.append(x.text)
                y = tds[4]
                gkpn_list.append(y.text)
                # print(gkpn_list)

                with open('gkpn.csv', 'a+', newline='') as file:
                    writer = csv.writer(file, delimiter='|')
                    writer.writerow(gkpn_list)

    else:
        print('ttttttttttttttttttttttt')
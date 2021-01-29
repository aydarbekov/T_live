import csv
import json
import os
import re
import time

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
import xml.etree.ElementTree as ET

with open('zakupki_tenders.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["Номер", "Закупающая организация", "Метод закупок", "Дата публикации",
                     "Срок подачи конкурсных заявок", "Гарантийное обеспечение конкурсной заявки",
                     "Наименование закупки", "Формат закупок", "Планируемая сумма", "Валюта конкурсной заявки",
                     "Срок действия конкурсных заявок", "Кол-во лотов"])

with open('zakupki_lots.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["Номер тендера", "Номер лота", "Наименование лота", "Сумма", "Адрес и Место поставки", "Условие поставки",
                     "Сроки поставки товара"])

with open('zakupki_products.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["Номер тендера", "Номер лота", "Класс ОКГЗ", "Единица измерения", "Количество", "Спецификации",
                     "Файл"])

with open('zakupki_submissions.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["Номер тендера", "Номер лота", "Сумма", "Название организации", "Валюта", "ГОКЗ", "Форма гокз", "Налог по сост на", "Налог статус", "Соц по сост на", "Соц статус"])

with open('zakupki_winners.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(["Номер тендера", "Номер лота", "Название организации", "Статус", "Предложенная сумма", "Причина отказа", "Планируемая сумма"])


def load_link(link, data):
    try:
        page = s.post(link, data=data, timeout=60)
        print(page.status_code)
        if page.status_code == 500 or page.status_code == 403:
            print('ОШИБКА, пробую еще через 5 сек')
            time.sleep(5)
            page = load_link(link, data)
    except Exception as e:
        print(e.args)
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link(link, data)
    return page


def load_link_header(link, data, header):
    try:
        page = s.post(link, data=data, headers=header, timeout=60)
        print(page.status_code)
        if page.status_code == 500 or page.status_code == 403:
            print('ОШИБКА, пробую еще через 5 сек')
            time.sleep(5)
            page = load_link(link, data)
    except Exception as e:
        print(e.args)
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link(link, data)
    return page

def load_link_get(link):
    try:
        page = s.get(link, timeout=60)
        print(page.status_code)

        if page.status_code == 500 or page.status_code == 403:
            print('ОШИБКА, пробую еще через 5 сек')
            time.sleep(5)
            page = load_link_get(link)
    except Exception as e:
        print(e.args)
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link_get(link)
    return page

s = requests.Session()

# q = s.get('http://zakupki.gov.kg')
a = s.get('http://zakupki.gov.kg/popp/view/order/list.xhtml')
bs_html = BeautifulSoup(a.text, 'html.parser')
# print(bs_html)
form = bs_html.find("form", {"id": "form"})
form_action = form['action']
# print(form_action)
cid = form_action.split('cid=')[1]
# print(cid)

viewstate_input = bs_html.find("input", {"name": "javax.faces.ViewState"})
viewstate = viewstate_input['value']
# print(viewstate)

tender_start = 3000

while True:
    data2=f'javax.faces.partial.ajax=true&javax.faces.source=j_idt113%3Aj_idt114%3Atable&javax.faces.partial.execute=j_idt113%3Aj_idt114%3Atable&javax.faces.partial.render=j_idt113%3Aj_idt114%3Atable&javax.faces.behavior.event=page&javax.faces.partial.event=page&j_idt113%3Aj_idt114%3Atable_pagination=true&j_idt113%3Aj_idt114%3Atable_first=10&j_idt113%3Aj_idt114%3Atable_rows=10&j_idt113%3Aj_idt114%3Atable_skipChildren=true&j_idt113%3Aj_idt114%3Atable_encodeFeature=true&j_idt113=j_idt113&j_idt113%3Aj_idt114%3Atable_rppDD=10&j_idt113%3Aj_idt114%3Atable_rppDD=10&j_idt113%3Aj_idt114%3Atable_selection=&j_idt113%3Aj_idt114_activeIndex=0&javax.faces.ViewState={viewstate}'
    data = {
    'javax.faces.partial.ajax': 'true',
    'javax.faces.source': 'j_idt113:j_idt114:table',
    'javax.faces.partial.execute': 'j_idt113:j_idt114:table',
    'javax.faces.partial.render': 'j_idt113:j_idt114:table',
    'javax.faces.behavior.event': 'page',
    'javax.faces.partial.event': 'page',
    'j_idt113:j_idt114:table_pagination': 'true',
    'j_idt113:j_idt114:table_first': str(tender_start),
    'j_idt113:j_idt114:table_rows': '1000',
    'j_idt113:j_idt114:table_skipChildren': 'true',
    'j_idt113:j_idt114:table_encodeFeature': 'true',
    'j_idt113': 'j_idt113',
    'j_idt113:j_idt114:table_rppDD': '10',
    'j_idt113:j_idt114:table_selection': '',
    'j_idt113:j_idt114_activeIndex': '0',
    'javax.faces.ViewState': viewstate
    }
    header = {
    'Accept': 'application/xml, text/xml, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '690',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=VwmIKFc81PEMEH7v8C7iXm7l2P3UEZSxuNt6GRHM.msc01-popp01:main-popp',
    'Faces-Request': 'partial/ajax',
    'Host': 'zakupki.gov.kg',
    'Origin': 'http://zakupki.gov.kg',
    'Referer': 'http://zakupki.gov.kg/popp/view/order/list.xhtml',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    print(viewstate)
    print(cid)
    # page = s.post(f'http://zakupki.gov.kg/popp/view/order/list.xhtml?cid={cid}', data=data)
    page = load_link(f'http://zakupki.gov.kg/popp/view/order/list.xhtml?cid={cid}', data)
    tender_start += 1000
    root = ET.fromstring(page.text)
    bs_lxml = BeautifulSoup(root[0][0].text, 'html.parser')
    trs = bs_lxml.find_all('tr')
    print('Кол-во обьявлений на странице', len(trs))
    count5 = 0
    for tr in trs:
        try:
            print(count5)
            count5 += 1
            print(tr['data-rk'])

            detail = load_link_get(f'http://zakupki.gov.kg/popp/view/order/view.xhtml?id={tr["data-rk"]}')

            bs_detail = BeautifulSoup(detail.text, 'html.parser')
            contents = bs_detail.find_all('div', {'class': 'container-content'})
            # print(len(contents))

            opening_protocol = contents[6].find('a', text='Протокол вскрытия')
            if opening_protocol:
                win = opening_protocol.find_next_sibling()
                if win:
                    print(win.text)
            # winning_protocol = contents[6].find('a', text=re.compile(r'Просмотр оценки конкурсной заявки'))
            # print(winning_protocol)



            # ОБЩИЕ ДАННЫЕ
            tender = []
            tenders_num = contents[0].find('span', text='Номер').find_next_sibling()
            print(tenders_num.text)
            tender.append(tenders_num.text)
            org_name = contents[0].find('span', text='Закупающая организация').find_next_sibling()
            print(org_name.text)
            tender.append(org_name.text)
            purchases_method = contents[0].find('span', text='Метод закупок').find_next_sibling()
            print(purchases_method.text)
            tender.append(purchases_method.text)
            date_start = contents[0].find('span', text='Дата публикации').find_next_sibling()
            print(date_start.text)
            tender.append(date_start.text)
            date_end = contents[0].find('span', text='Срок подачи конкурсных заявок').find_next_sibling()
            print(date_end.text)
            tender.append(date_end.text)
            gokz_sibling = contents[0].find('span', text='Гарантийное обеспечение конкурсной заявки')
            if gokz_sibling:
                gokz = gokz_sibling.find_next_sibling().text
            else:
                gokz = ''
            print(gokz)
            tender.append(gokz)
            purchases_name = contents[0].find('span', text='Наименование закупки').find_next_sibling()
            print(purchases_name.text)
            tender.append(gokz)
            purchases_format = contents[0].find('span', text='Формат закупок').find_next_sibling()
            print(purchases_format.text)
            tender.append(purchases_format.text)
            planned_amount = contents[0].find('span', text='Планируемая сумма').find_next_sibling()
            print(planned_amount.text)
            tender.append(planned_amount.text)
            valuta = contents[0].find('span', text='Валюта конкурсной заявки').find_next_sibling()
            print(valuta.text)
            tender.append(valuta.text)
            validity = contents[0].find('span', text='Срок действия конкурсных заявок').find_next_sibling()
            if validity:
                validity = validity.text
            else:
                validity = ''
            print(validity)
            tender.append(validity)


            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!---ЛОТЫ---!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



            lot_trs = contents[2].find('tbody').find_all('tr')
            print('Кол-во лотов - ', len(lot_trs))
            tender.append(len(lot_trs))
            with open('zakupki_tenders.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerow(tender)


            lot_counter = 0
            for lot_tr in lot_trs:
                lot = []
                print(tenders_num.text)
                lot.append(tenders_num.text)
                lots_number = lot_tr.find('span', text='№')
                if lots_number:
                    lots_number = lots_number.find_next_sibling()
                if not lots_number:
                    lots_number = lot_tr.find('span', text='#').find_next_sibling()
                print(lots_number.text)
                lot.append(lots_number.text)
                lots_name = lot_tr.find('span', text='Наименование лота').find_next_sibling()
                print(lots_name.text)
                lot.append(lots_name.text)
                lots_amount = lot_tr.find('span', text='Сумма').find_next_sibling()
                print(lots_amount.text)
                lot.append(lots_amount.text)
                address = lot_tr.find('span', text='Адрес и Место поставки')
                if address:
                    address = address.find_next_sibling()
                elif not address:
                    address = lot_tr.find('span', text='Адрес и Место работ / услуг').find_next_sibling()
                print(address.text.rstrip())
                lot.append(address.text.rstrip())
                condition = lot_tr.find('span', text='Условие поставки')
                if condition:
                    condition = condition.find_parent().text
                if not condition:
                    condition = lot_tr.find('span', text='Срок выполнения работ ').find_parent().find(text=True, recursive=False)
                print(condition)
                lot.append(condition)
                timing = lot_tr.find('span', text='Сроки поставки товара ')
                if timing:
                    timing = timing.find_next_sibling().text
                    print(timing)
                else:
                    timing = ''
                lot.append(timing)

                with open('zakupki_lots.csv', 'a+', newline='') as file:
                    writer = csv.writer(file, delimiter='|')
                    writer.writerow(lot)

            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!---ТОВАРЫ---!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                viewstate_input2 = bs_detail.find("input", {"name": "javax.faces.ViewState"})
                viewstate2 = viewstate_input2['value']
                form2 = bs_detail.find("form", {"id": "j_idt34"})
                form_action2 = form2['action']
                cid2 = form_action2.split('cid=')[1]
                tbody = bs_detail.find('tbody')
                tbody_id_full = tbody['id']
                tbody_id = tbody_id_full[:-5]

                # print(tbody_id)
                data3 = f'javax.faces.partial.ajax=true&javax.faces.source={tbody_id}&javax.faces.partial.execute={tbody_id}&javax.faces.partial.render={tbody_id}&j_idt78%3AlotsTable={tbody_id}&j_idt78%3AlotsTable_rowExpansion=true&j_idt78%3AlotsTable_expandedRowIndex=0&j_idt78%3AlotsTable_encodeFeature=true&j_idt78%3AlotsTable_skipChildren=true&j_idt76=j_idt76&j_idt78%3Atender-doc-explanation-table_rppDD=10&j_idt78%3Atender-doc-explanation-table_selection=&j_idt78_activeIndex=0&javax.faces.ViewState={viewstate}'
                data_lot = {
                    'javax.faces.partial.ajax': 'true',
                    'javax.faces.source': tbody_id,
                    'javax.faces.partial.execute': tbody_id,
                    'javax.faces.partial.render': tbody_id,
                    tbody_id: tbody_id,
                    f'{tbody_id}_rowExpansion': 'true',
                    f'{tbody_id}_expandedRowIndex': str(lot_counter),
                    f'{tbody_id}_encodeFeature': 'true',
                    f'{tbody_id}_skipChildren': 'true',
                    'j_idt76': 'j_idt76',
                    'j_idt78: tender - doc - explanation - table_rppDD': 10,
                    'j_idt78: tender - doc - explanation - table_selection': '',
                    'j_idt78_activeIndex': '0',
                    'javax.faces.ViewState': viewstate2
                }

                lot = load_link(f'http://zakupki.gov.kg/popp/view/order/view.xhtml?cid={cid2}', data_lot)
                lot_counter += 1
                # print(lot.text)
                lot_text = lot.text
                # print(lot_text)
                root2 = ET.fromstring(lot_text)
                bs_lot = BeautifulSoup(root2[0][0].text, 'html.parser')
                print('-------------------ЛОТ----------------------')
                # print(bs_lot.prettify())
                table = bs_lot.find('table', {'class': 'display-table private-room-table no-borders f-right'})
                prod_trs = table.find('tbody').find_all('tr')
                for prod_tr in prod_trs:
                    product = []
                    product.append(tenders_num.text)
                    product.append(lots_number.text)
                    # print(prod_tr)
                    fields = prod_tr.find_all('td')

                    okgz = fields[0]
                    print(okgz.text)
                    product.append(okgz.text)
                    measure = fields[1]
                    print(measure.text)
                    product.append(measure.text)
                    count = fields[2]
                    print(count.text)
                    product.append(count.text)
                    specification = fields[3]
                    print(specification.text)
                    product.append(specification.text)
                    file = fields[4].find('a')
                    if file:
                        file = file['href']
                    else:
                        file = ''
                    product.append(file)

                    with open('zakupki_products.csv', 'a+', newline='') as file:
                        writer = csv.writer(file, delimiter='|')
                        writer.writerow(product)


            # !!!!!!!!!!!!!!!!!!!!!! -- ПРОТОКОЛ ВСКРЫТИЯ --- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


            if opening_protocol:
                # os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!ЕСТЬ ПРОТОКОЛ ВСКРЫТИЯ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                # time.sleep(5)
                viewstate_input2 = bs_detail.find("input", {"name": "javax.faces.ViewState"})
                viewstate2 = viewstate_input2['value']
                print(viewstate2)
                print(tr["data-rk"])
                form3 = bs_detail.find("form", {"id": "j_idt34"})
                form_action3 = form3['action']
                cid3 = form_action3.split('cid=')[1]
                print(cid3)
                print(f'http://zakupki.gov.kg/popp/view/order/view.xhtml?cid={cid3}')
                data_opening = {
                    'j_idt76': 'j_idt76',
                    'j_idt78:tender-doc-explanation-table_rppDD': '10',
                    'j_idt78:tender-doc-explanation-table_selection': '',
                    'j_idt78_activeIndex': '0',
                    'javax.faces.ViewState': viewstate2,
                    'j_idt78:contest': 'j_idt78:contest',
                }
                header3 = {
                    'Accept': 'text/html, application/xhtml + xml, application / xml;q = 0.9, image / avif, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
                    'Accept - Encoding': 'gzip, deflate',
                    'Accept - Language': 'ru - RU, ru;q = 0.9',
                    'Cache - Control': 'max - age = 0',
                    'Connection': 'keep - alive',
                    'Content - Length': '237',
                    'Content - Type': 'application / x - www - form - urlencoded',
                    # 'Cookie: JSESSIONID = DBn4c5 - ZhtLYF - PuaOfdbOHgafb4uq8djdIkgl5W.msc01 - popp01:main - popp
                    'Host': 'zakupki.gov.kg',
                    'Origin': 'http: // zakupki.gov.kg',
                    'Referer': f'http://zakupki.gov.kg/popp/view/order/view.xhtml?id={tr["data-rk"]}',
                    'Upgrade - Insecure - Requests': '1',
                    'User - Agent': 'Mozilla / 5.0(X11;Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 87.0.4280.88 Safari / 537.36'
                }
                opening = load_link_header(f'http://zakupki.gov.kg/popp/view/order/view.xhtml?cid={cid3}', data_opening, header3)
                if opening.status_code == 500:
                    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
                    print(tr["data-rk"])
                    with open('error_p.csv', 'a+', newline='') as file:
                        writer = csv.writer(file)
                        writer.write(tr["data-rk"])
                        writer.write('Не зашел во вскрытие')
                    continue
                # print(opening.text)
                bs_submissions = BeautifulSoup(opening.text, 'html.parser')
                trs = bs_submissions.find('tbody', {'id': 'submissions_data'}).find_all('tr', recursive=False)
                print(len(trs))
                for tr in trs:
                    submission = []
                    submission.append(tenders_num.text)

                    no_data = tr.find('td', text='Не найдено ни одной записи.')
                    if no_data:
                        print('НЕТ УЧАСТНИКОВ')
                        break
                    # print(tr)
                    print('!!!!!!!!!!!!!!!!!!!!!!!!!')
                    tds = tr.findAll('td', recursive=False)
                    lots = tds[2].find_all('table')
                    for lot in lots:
                        lot_detail = lot.find_all('td')
                        lot_number = lot_detail[0]
                        submission.append(lot_number.text.split(' :')[0])
                        print(lot_number.text)
                        lot_sum = lot_detail[2]
                        print(lot_sum.text)
                        submission.append(lot_sum.text)
                        org_name = (tds[1].text).strip(' \n\r')
                        submission.append(org_name)
                        print(org_name)
                        valuta_submission = (tds[3].text).strip(' \n\r')
                        print(valuta_submission)
                        submission.append(valuta_submission)
                        gokz_submission = (tds[4].text).strip(' \n\r')
                        submission.append(gokz_submission)
                        print(gokz_submission)
                        gokz_form_submission = (tds[5].text).strip(' \n\r')
                        submission.append(gokz_form_submission)
                        print(gokz_form_submission)
                        tax_date_submission = (tds[6].text).strip(' \n\r')
                        submission.append(tax_date_submission)
                        print(tax_date_submission)
                        tax_status_submission = (tds[7].text).strip(' \n\r')
                        submission.append(tax_status_submission)
                        print(tax_status_submission)
                        soc_date_submission = (tds[8].text).strip(' \n\r')
                        submission.append(soc_date_submission)
                        print(soc_date_submission)
                        soc_status_submission = (tds[8].text).strip(' \n\r')
                        submission.append(soc_status_submission)
                        print(soc_status_submission)
                        with open('zakupki_submissions.csv', 'a+', newline='') as file:
                            writer = csv.writer(file, delimiter='|')
                            writer.writerow(submission)



                data_winners = {
                    'j_idt76': 'j_idt76',
                    'j_idt78:tender-doc-explanation-table_rppDD': '10',
                    'j_idt78:tender-doc-explanation-table_selection': '',
                    'j_idt78_activeIndex': '0',
                    'javax.faces.ViewState': viewstate2,
                    'j_idt78:contest': 'j_idt78:contest',
                    'j_idt78:j_idt557': 'j_idt78: j_idt557',
                }
                data_winners2 = {
                    'j_idt233': 'j_idt233',
                    'j_idt233:j_idt234': '',
                    'javax.faces.ViewState': viewstate2
                }

                # winning_protocol = contents[6].find('a', text='Просмотр оценки конкурсной заявки')
                print('ОЦЕНКА')
                if win:
                    if 'Просмотр оценки конкурсной заявки' in win.text:
                        winners = load_link_header(f'http://zakupki.gov.kg/popp/view/order/view.xhtml?cid={cid3}', data_winners, header3)
                        # print(winners.text)
                        if winners.status_code == 500:
                            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
                            print(tr["data-rk"])
                            with open('error_p.csv', 'a+', newline='') as file:
                                writer = csv.writer(file)
                                writer.write(tr["data-rk"])
                                writer.write('Не зашел к победителям')
                            continue
                        bs_winners = BeautifulSoup(winners.text, 'html.parser')
                        table_winners = bs_winners.find('tbody', {'id': 'table_data'})
                        trs_winners = table_winners.find_all('tr')
                        for tr_winner in trs_winners:
                            tds_winners = tr_winner.find_all('td')
                            winner_lot = tds_winners[1].text

                            winners_sum = tds_winners[4].text
                            print(winners_sum)
                            winners_cancelled_prichina = tds_winners[5].text
                            print(winners_cancelled_prichina)
                            planed_sum = tds_winners[6].text
                            print(planed_sum)
                            winners = tds_winners[3].find_all('li')
                            for winner in winners:
                                winner_list = []
                                winner_list.append(tenders_num.text)
                                print(tenders_num.text)
                                winner_list.append(winner_lot)
                                print(winner_lot, 'dfdfdfdf')
                                winner_name = winner.find_all('span')[0]
                                winner_list.append(winner_name.text)
                                print(winner_name.text)
                                try:
                                    winner_status = winner.find_all('span')[1]
                                    winner_list.append(winner_status.text)
                                    print(winner_status.text)
                                except:
                                    # winner_status_2 = tds_winners[3].find_all('li')
                                    # winner_list.append(winner_status_2)
                                    # print(winner_status_2)
                                    winner_list.append('(Ожидается подтверждения)')
                                    print('dfsfsd----------------------------------------------------------')
                                winner_list.append(winners_sum)
                                winner_list.append(winners_cancelled_prichina)
                                winner_list.append(planed_sum)
                                with open('zakupki_winners.csv', 'a+', newline='') as file:
                                    writer = csv.writer(file, delimiter='|')
                                    writer.writerow(winner_list)
        except Exception as e:
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
            print(e)
            print('какая то ошибка и идем дальше')
            with open('error_p.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerow(tr["data-rk"])



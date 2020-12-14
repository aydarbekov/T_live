import csv
import time

import requests
from bs4 import BeautifulSoup

# with open('minjust_8.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerow(["Полное наименование кг", "Полное наименование ру", "сокр наименование кг", "Сокращенное наименование ру", "Орган прав форма", "Иностр участие",
#                      "Рег номер", "ОКПО", "ИНН", "Область", "Район", "Город село поселок", "мкрн", "улица",
#                      "Номер дома", "Номер кв", "Тел", "Факс", "Почта", "Рег или перерег", "Дата приказа", "Дата перв регистр", "Способ создания", "Форма собственности", "Директор", "Основн вид деят", "Код экон деят",
#                      "кол-во учред физ", "Кол-во учред юр", "Общ кол-во учред", "Учредители", "Ссылка на сайт"])

def load_link(link):
    try:
        page = requests.get(link, timeout=10)
    except:
        print('SOME ERROR!!!!!!!!!!! RETRY AFTER 10 SEC')
        time.sleep(10)
        page = load_link(link)
    return page
count = 79025


while True:
    print(count)
    if count == 80000:
        break
    firm_info = []
    main = load_link(f'https://register.minjust.gov.kg/register/SearchAction.seam?firstResult={count}&logic=and&cid=4738576')
    count += 25
    bs_html = BeautifulSoup(main.text, 'html.parser')
    trs = bs_html.find('tbody').findAll('tr')
    for tr in trs:
        link = tr.find('a')
        href = link.get('href')
        detail = load_link('https://register.minjust.gov.kg/' + href)
        detail_html = BeautifulSoup(detail.text, 'html.parser')
        sibling_full_kg_name_ = detail_html.find('span', text='1. Полное наименование(на государственном языке)')
        full_kg_name = sibling_full_kg_name_.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not full_kg_name:
            full_kg_name = ''
        else:
            full_kg_name = full_kg_name.text
        sibling_full_ru_name_ = detail_html.find('span', text='2. Полное наименование на официальном языке')
        full_ru_name = sibling_full_ru_name_.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not full_ru_name:
            full_ru_name = ''
        else:
            full_ru_name = full_ru_name.text
        sibling_short_kg_name_ = detail_html.find('span', text='3. Сокрашенное наименование(на государственном языке)')
        short_kg_name = sibling_short_kg_name_.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not short_kg_name:
            short_kg_name = ''
        else:
            short_kg_name = short_kg_name.text
        sibling_short_ru_name_ = detail_html.find('span', text='4. Сокрашенное наименование(на официальном языке)')
        short_ru_name = sibling_short_ru_name_.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not short_ru_name:
            short_ru_name = ''
        else:
            short_ru_name = short_ru_name.text
        sibling_org_form = detail_html.find('span', text='5. Организационно-правовая форма')
        org_form = sibling_org_form.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not org_form:
            org_form = ''
        else:
            org_form = org_form.text
        sibling_foreign_founders = detail_html.find('span', text='6. Есть ли иностранное участие')
        foreign_founders = sibling_foreign_founders.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not foreign_founders:
            foreign_founders = ''
        else:
            foreign_founders = foreign_founders.text
        sibling_registration_number = detail_html.find('span', text='7. Регистрационный номер')
        registration_number = sibling_registration_number.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not registration_number:
            registration_number = ''
        else:
            registration_number = registration_number.text
        sibling_okpo_cod = detail_html.find('span', text='8. Код ОКПО')
        okpo_cod_siblings = sibling_okpo_cod.find_parent().find_parent().find_parent().find_next_sibling().findChildren(recursive=False)
        okpo_cod = okpo_cod_siblings[2]
        if not okpo_cod:
            okpo_cod = ''
        else:
            okpo_cod = okpo_cod.text
        sibling_inn = detail_html.find('span', text='9. ИНН')
        inn = sibling_inn.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not inn:
            inn = ''
        else:
            inn = inn.text
        sibling_address_region = detail_html.find('span', text='10. Область')
        address_region = sibling_address_region.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not address_region:
            address_region = ''
        else:
            address_region = address_region.text
        sibling_address_district = detail_html.find('span', text='11. Район')
        address_district = sibling_address_district.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not address_district:
            address_district = ''
        else:
            address_district = address_district.text
        sibling_address_city = detail_html.find('span', text='12. Город/село/поселок')
        address_city = sibling_address_city.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not address_city:
            address_city = ''
        else:
            address_city = address_city.text
        sibling_address_microdistrict = detail_html.find('span', text='13. Микрорайон')
        address_microdistrict = sibling_address_microdistrict.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not address_microdistrict:
            address_microdistrict = ''
        else:
            address_microdistrict = address_microdistrict.text
        sibling_address_street = detail_html.find('span', text='14. Улица (проспект, бульвар, переулок и т.п.)')
        address_street = sibling_address_street.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not address_street:
            address_street = ''
        else:
            address_street = address_street.text
        sibling_house_number = detail_html.find('span', text='15. № дома')
        house_number = sibling_house_number.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not house_number:
            house_number = ''
        else:
            house_number = house_number.text
        sibling_apartment_number = detail_html.find('span', text='15. № дома')
        apartment_number = sibling_apartment_number.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not apartment_number:
            apartment_number = ''
        else:
            apartment_number = apartment_number.text
        sibling_phone = detail_html.find('span', text='17. Телефон')
        phone = sibling_phone.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not phone:
            phone = ''
        else:
            phone = phone.text
        sibling_fax = detail_html.find('span', text='18. Факс')
        fax = sibling_fax.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not fax:
            fax = ''
        else:
            fax = fax.text
        sibling_email = detail_html.find('span', text='19. Электронный адрес')
        email = sibling_email.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not email:
            email = ''
        else:
            email = email.text
        sibling_reg_or_rereg = detail_html.find('span', text='20. Государственная (учетная) регистрация или перерегистрация')
        reg_or_rereg = sibling_reg_or_rereg.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not reg_or_rereg:
            reg_or_rereg = ''
        else:
            reg_or_rereg = reg_or_rereg.text
        sibling_order_date = detail_html.find('span', text='21. Дата приказа')
        order_date = sibling_order_date.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not order_date:
            order_date = ''
        else:
            order_date = order_date.text
        sibling_first_reg_date = detail_html.find('span', text='22. Дата первичной регистрации (в случае государственной перерегистрации)')
        reg_date = sibling_first_reg_date.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not reg_date:
            reg_date = ''
        else:
            reg_date = reg_date.text
        sibling_creation_method = detail_html.find('span', text='23. Способ создания')
        creation_method = sibling_creation_method.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not creation_method:
            creation_method = ''
        else:
            creation_method = creation_method.text
        sibling_type_of_ownership = detail_html.find('span', text='24. Форма собственности')
        type_of_ownership = sibling_type_of_ownership.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not type_of_ownership:
            type_of_ownership = ''
        else:
            type_of_ownership = type_of_ownership.text
        sibling_director = detail_html.find('span', text='25. Фамилия, имя, отчество')
        director = sibling_director.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not director:
            director = ''
        else:
            director = director.text
        sibling_main_activity = detail_html.find('span', text='26. Основной вид деятельности')
        main_activity = sibling_main_activity.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not main_activity:
            main_activity = ''
        else:
            main_activity = main_activity.text
        sibling_economic_activity_cod = detail_html.find('span', text='27. Код экономической деятельности')
        economic_activity_cod = sibling_economic_activity_cod.find_parent().find_parent().find_parent().find_previous_sibling().findChildren(recursive=False)[1]
        if not economic_activity_cod:
            economic_activity_cod = ''
        else:
            economic_activity_cod = economic_activity_cod.text
        sibling_count_of_founders_ind = detail_html.find('span', text='28. Количество учредителей (участников) - физических лиц')
        count_of_founders_ind = sibling_count_of_founders_ind.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not count_of_founders_ind:
            count_of_founders_ind = ''
        else:
            count_of_founders_ind = count_of_founders_ind.text
        sibling_count_of_founders_legal = detail_html.find('span', text='29. Количество учредителей (участников) - юридических лиц')
        count_of_founders_legal = sibling_count_of_founders_legal.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not count_of_founders_legal:
            count_of_founders_legal = ''
        else:
            count_of_founders_legal = count_of_founders_legal.text
        sibling_total_count_of_founders = detail_html.find('span', text='30. Общее количество учредителей (участников)')
        total_count_of_founders = sibling_total_count_of_founders.find_parent().find_parent().find_next_sibling().find_next_sibling()
        if not total_count_of_founders:
            total_count_of_founders = ''
        else:
            total_count_of_founders = total_count_of_founders.text
        sibling_founders = detail_html.findAll('span', text='Учредитель (участник)')
        founders_list = []
        if sibling_founders:
            for sibling_founder in sibling_founders:
                founder = sibling_founder.find_parent().find_parent().find_next_sibling().find_next_sibling()
                # print(founder.text)
                founders_list.append(founder.text)
        print('https://register.minjust.gov.kg/' + href)
        with open('minjust_8.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([full_kg_name, full_ru_name, short_kg_name,
                             short_ru_name, org_form, foreign_founders,
                             registration_number, okpo_cod, inn, address_region,
                             address_district, address_city, address_microdistrict, address_street,
                             house_number, apartment_number, phone, fax, email,
                             reg_or_rereg, order_date,
                             reg_date, creation_method, type_of_ownership, director,
                             main_activity, economic_activity_cod,
                             count_of_founders_ind, count_of_founders_legal, total_count_of_founders, founders_list, 'https://register.minjust.gov.kg/' + href])


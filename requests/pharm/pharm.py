import csv
import os

import requests
from bs4 import BeautifulSoup

os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
countries = [
    'Абхазия',
    'Австралия',
    'Австрия',
    'Азербайджан',
    'Албания',
    'Алжир',
    'Ангола',
    'Андорра',
    'Антигуа и Барбуда',
    'Аргентина',
    'Армения',
    'Афганистан',
    'Багамские Острова',
    'Бангладеш',
    'Барбадос',
    'Бахрейн',
    'Белиз',
    'Белоруссия',
    'Бельгия',
    'Бенин',
    'Болгария',
    'Боливия',
    'Босния и Герцеговина',
    'Ботсвана',
    'Бразилия',
    'Бруней',
    'Буркина-Фасо',
    'Бурунди',
    'Бутан',
    'Вануату',
    'Ватикан',
    'Великобритания',
    'Венгрия',
    'Венесуэла',
    'Восточный Тимор',
    'Вьетнам',
    'Габон',
    'Гаити',
    'Гайана',
    'Гамбия',
    'Гана',
    'Гватемала',
    'Гвинея',
    'Гвинея-Бисау',
    'Германия',
    'Гондурас',
    'Государство Палестина',
    'Гренада',
    'Греция',
    'Грузия',
    'Дания',
    'Джибути',
    'Доминика',
    'Доминиканская Республика',
    'ДР Конго',
    'Египет',
    'Замбия',
    'Зимбабве',
    'Израиль',
    'Индия',
    'Индонезия',
    'Иордания',
    'Ирак',
    'Иран',
    'Ирландия',
    'Исландия',
    'Испания',
    'Италия',
    'Йемен',
    'Кабо-Верде',
    'Казахстан',
    'Камбоджа',
    'Камерун',
    'Канада',
    'Катар',
    'Кения',
    'Кипр',
    'Киргизия',
    'Кирибати',
    'Китай',
    'КНДР',
    'Колумбия',
    'Коморские Острова',
    'Коста-Рика',
    'Кот-д"Ивуар",'
    'Куба',
    'Кувейт',
    'Лаос',
    'Латвия',
    'Лесото',
    'Либерия',
    'Ливан',
    'Ливия',
    'Литва',
    'Лихтенштейн',
    'Люксембург',
    'Маврикий',
    'Мавритания',
    'Мадагаскар',
    'Малави',
    'Малайзия',
    'Мали',
    'Мальдивские Острова',
    'Мальта',
    'Марокко',
    'Маршалловы Острова',
    'Мексика',
    'Мозамбик',
    'Молдавия',
    'Монако',
    'Монголия',
    'Мьянма',
    'Намибия',
    'Науру',
    'Непал',
    'Нигер',
    'Нигерия',
    'Нидерланды',
    'Никарагуа',
    'Новая Зеландия',
    'Норвегия',
    'ОАЭ',
    'Оман',
    'Пакистан',
    'Палау',
    'Панама',
    'Папуа - Новая Гвинея',
    'Парагвай',
    'Перу',
    'Польша',
    'Португалия',
    'Республика Конго',
    'Республика Корея',
    'Россия',
    'Руанда',
    'Румыния',
    'Сальвадор',
    'Самоа',
    'Сан-Марино',
    'Сан-Томе и Принсипи',
    'Саудовская Аравия',
    'Северная Македония',
    'Сейшельские Острова',
    'Сенегал',
    'Сент-Винсент и Гренадины',
    'Сент-Китс и Невис',
    'Сент-Люсия',
    'Сербия',
    'Сингапур',
    'Сирия',
    'Словакия',
    'Словения',
    'Соломоновы Острова',
    'Сомали',
    'Судан',
    'Суринам',
    'США',
    'Сьерра-Леоне',
    'Таджикистан',
    'Таиланд',
    'Танзания',
    'Того',
    'Тонга',
    'Тринидад и Тобаго',
    'Тувалу',
    'Тунис',
    'Туркмения',
    'Турция',
    'Уганда',
    'Узбекистан',
    'Украина',
    'Уругвай',
    'Федеративные Штаты Микронезии',
    'Фиджи',
    'Филиппины',
    'Финляндия',
    'Франция',
    'Хорватия',
    'ЦАР',
    'Чад',
    'Черногория',
    'Чехия',
    'Чили',
    'Швейцария',
    'Швеция',
    'Шри-Ланка',
    'Эквадор',
    'Экваториальная Гвинея',
    'Эритрея',
    'Эсватини',
    'Эстония',
    'Эфиопия',
    'ЮАР',
    'Южная Осетия',
    'Южный Судан',
    'Ямайка',
    'Япония',

]

with open('pharm.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['Наименование', "Инструкция", "МНН", "Лекарственная форма", "Дозировка", "Фасовка",
                     "Предприятие производитель", 'Страна производства', 'Держатель свидетельства',
                     'Страна держателя свидетельства', 'АТХ', 'Фармакотерапевтическая группа', 'ПЖВЛС',
                     'Условия отпуска из аптек', '№ свидетельства', 'Дата выдачи', 'EAN13'])

for coun in countries:
    print(coun)
    data = {
        'name': '',
        'mnn': '',
        'proizvod': coun,
        'ftg': '',
        'ath': '',
        'ean': '',
    }

    pharm_page = requests.post("http://212.112.103.101/reestr", data=data)
    bs_pharm = BeautifulSoup(pharm_page.text, 'html.parser')
    body = bs_pharm.find('tbody')
    if body:
        trs = body.find_all('tr')
    else:
        continue
    counter = 0

    for tr in trs:
        counter += 1
        pharm = []
        print(tr)
        print(counter)
        tds = tr.find_all('td')
        print(tds)
        print(len(tds))
        name = tds[0]
        pharm.append(name.text)
        instruction = tds[1]
        pharm.append(instruction.text)
        mnn = tds[2]
        pharm.append(mnn.text)
        lec_form = tds[3]
        pharm.append(lec_form.text)
        dozirovka = tds[4]
        pharm.append(dozirovka.text)
        fasovka = tds[5]
        pharm.append(fasovka.text)
        made_in = tds[6]
        pharm.append(made_in.text)
        country = tds[7]
        pharm.append(country.text)
        keeper = tds[8]
        pharm.append(keeper.text)
        country_keeper = tds[9]
        pharm.append(country_keeper.text)
        ath = tds[10]
        pharm.append(ath.text)
        farm_group = tds[11]
        pharm.append(farm_group.text)
        pjvls = tds[12]
        pharm.append(pjvls.text)
        uslovia = tds[13]
        pharm.append(uslovia.text)
        number_cert = tds[14]
        pharm.append(number_cert.text)
        date = tds[15]
        pharm.append(date.text)
        ean13 = tds[16]
        pharm.append(ean13.text)

        with open('pharm.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(pharm)

import csv
import time
# from bs4 import BeautifulSoup
import openpyxl
import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import csv

import os

all_rows_not_parsed = []
all_rows = [
'https://www.facebook.com/profile.php?id=100041921119187',
]

# with open('all_com.csv', 'r', newline='') as file:
#     rows = csv.reader(file, delimiter='|')
#     for row in rows:
#         all_rows_not_parsed.append(row)

asd = 0
repeated = 0


# for row in all_rows_not_parsed:
#     if 'php?id' in row[1] and '&' in row[1]:
#         splited = row[1].split('&')
#         row[1] = splited[0]
#     elif 'groups' in row[1]:
#         splited = row[1].split('/?__cft__')
#         row[1] = splited[0]

#     all_rows.append(row)


#     else:
#         splited = row[1].split('?')
#         row[1] = splited[0]
#     all_rows.append(row)
#     print(row[1])
#     all_rows.append(row)


repeated_links = []
errored_links = []



# with open('fb_profile.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerow(["Ссылка", "Имя", "кол-во постов", "дата последнего поста", "фото профиля", "размер фото",
#                      "Работа", "ВУЗ", "Школа", "Адрес", "Контакты", "Сайты и соцсети", "Осн инфо", "Дата рождения",
#                      "Язык", "Статус", "Семья", "О пользователе", "Произношение имени", "Другие имена", "Цитаты", "кол-во фото из хрон", "Кол-во фоток", "кол-во нравится", "Отметки нравится", "Кол-во друзей", "Друзья"])



def parse_info(xpath):
    infos = []
    objects = driver.find_elements_by_xpath(xpath)
    for object in objects:
        print(object.text)
        infos.append(object.text)
    profile_info.append(infos)


def scroll_to_down(divs, time_plus, ogr):
    time_wait = 2
    retry = 0
    while True:
        p_height = driver.execute_script("return document.body.scrollHeight;")
        print(p_height)
        driver.execute_script(f"window.scrollTo(0, (document.body.scrollHeight)/2);")
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(time_wait + time_plus)
        new_p_height = driver.execute_script("return document.body.scrollHeight;")
        print(new_p_height)
        print(p_height == new_p_height)
        objects = driver.find_elements_by_xpath(divs)
        print(len(objects))
        if ogr == 'posts':
            if len(objects) > 1000:
                break
        #     time_wait = 5 + time_plus
        # elif len(objects) > 1000:
        #     time_wait = 7 + time_plus
        # elif len(objects) > 1500:
        #     time_wait = 10 +time_plus
        if p_height == new_p_height:
            if retry < 3:
                retry += 1
                print('retryyyyyyy')
                pass
            else:
                print('end')
                break
        else:
            retry = 0
    profile_info.append(len(objects))



option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# option.add_argument("--headless")
option.add_argument("--window-size=1325x744")
option.add_argument("--remote-debugging-port=9221")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option)
# driver.maximize_window(driver.window_handles)
# driver.window_handles
print('Захожу на фб')
driver.get("https://www.facebook.com")
driver.implicitly_wait(10)
# time.sleep(2)

# print('Жму на закрытие окоша модалки')
# WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-cookiebanner="accept_button"]'))).click()

# driver.implicitly_wait(10)
# time.sleep(1)

print("Логинюсь")
driver.find_element_by_name('email').send_keys('azamatsatynbekov@gmail.com')
driver.find_element_by_name('pass').send_keys('aselsatkotoma123')



print("Отправляю форму")
time.sleep(2)
driver.find_element_by_css_selector('button[type="submit"]').click()

driver.implicitly_wait(10)
time.sleep(2)
count_row = 0
for row in all_rows:

    print(row)
    row = row.split('|')

    count_row += 1
    print(count_row)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # if count_row < 730:
    #     continue
    try:
        print(row[1])
        print(repeated_links)
        profile_info = []
        for elem in row:
            profile_info.append(elem)
        if row[1] not in repeated_links:
            repeated_links.append(row[1])
        else:
            print('дубликат иду дальше')
            repeated += 1
            print(repeated, 'Дубликатов')
            with open('fb_profile.csv', 'a+', newline='') as file:
                writer = csv.writer(file, delimiter='|')
                writer.writerow(profile_info)
            continue
        print("Захожу на профиль")
        driver.get(row)
        driver.implicitly_wait(10)
        time.sleep(7)
        try:
            short_info = driver.find_element_by_xpath("//div[@class='sjgh65i0'][1]/div[@class='j83agx80 l9j0dhe7 k4urcfbm']//div[@class='sej5wr8e']")
            profile_info.append(short_info.text)
            print(short_info.text)
            print("Try short info")
        except:
            profile_info.append('not')
            print('Not short info')
        time.sleep(3)
        try:
            print('недоступен ли')
            driver.implicitly_wait(0)
            deleted = driver.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i o3w64lxj b2s5l15y hnhda86s m9osqain oqcyycmt']")
            driver.implicitly_wait(0)
            if deleted.text == 'Этот контент сейчас недоступен':
                profile_info.append('НЕ ДОСТУПЕН')
                with open('fb_profile.csv', 'a+', newline='') as file:
                    writer = csv.writer(file, delimiter='|')
                    writer.writerow(profile_info)
                continue
        except:
            pass
        try:
            time.sleep(3)
            print('try')
            full_profile = driver.find_element_by_css_selector('a[aria-label="Посмотреть основной профиль"]')
            try:
                short_info = driver.find_element_by_xpath(
                    "//div[@class='sjgh65i0'][1]/div[@class='j83agx80 l9j0dhe7 k4urcfbm']//div[@class='sej5wr8e']")
                profile_info.append(short_info.text)
                print("Нашел инфо с какого в группе")
                print(short_info.text)
            except:
                print('Нет инфо о группе')
                profile_info.append('not')
            full_profile.click()
            time.sleep(7)

        except:
            print('Нет инфо о группе')
            profile_info.append('not')
            print('pass')

            pass


        time.sleep(1)
        try:
            short_info_in_main = driver.find_element_by_xpath(".//*[contains(text(), 'Краткая информация')]/../../../../../../../..")
            registration = short_info_in_main.find_element_by_xpath(".//*[contains(text(), 'На Facebook с:')]")
            profile_info.append(registration.text)
            print(registration.text)
        except:
            print('Нет даты регистрации')
            profile_info.append('Нет даты регистрации')

        name_h1 = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t gs1a9yip owycx6da btwxx1t3 ihqw7lf3 cddn0xzi']")
        print(name_h1.text)
        profile_info.append(name_h1.text)


        # парсинг постов
        print("Парсю посты")
        post_divs = "//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div"
        try:
            post = driver.find_element_by_xpath(".//*[contains(text(), 'Нет доступных публикаций')]")
            profile_info.append('0')
            profile_info.append(post.text)
        except:
            scroll_to_down(post_divs, 2, 'posts')
            try:
                print('1ая попытка')
                last_post = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[last()]")
                time_post = last_post.find_element_by_css_selector('a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]')
            except:
                print('2ая попытка')
                last_post = driver.find_element_by_xpath(
                    "//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[last()-3]")
                time_post = last_post.find_element_by_css_selector(
                    'a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]')

            driver.execute_script(f"window.scrollTo(0, 0);")
            # time.sleep(3)
            print('хочу навести на дату')
            hover = ActionChains(driver).move_to_element(time_post)
            hover.perform()
            print('навел')
            time.sleep(1)
            try:
                print('ищу черный див')
                time_full = driver.find_element_by_css_selector(
                    'span[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 tia6h79c fe6kdd0r mau55g9w c8b282yb iv3no6db e9vueds3 j5wam9gi knj5qynh oo9gr5id hzawbc8m"]')
                print(time_full.text)
                profile_info.append(time_full.text)

            except:
                print("не нашел черный див")
                try:
                    time_icon = last_post.find_element_by_css_selector(
                        'span[class="tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41"]')
                    prelast_post = driver.find_element_by_xpath(
                        "//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[last()-1]")
                    time_post = prelast_post.find_element_by_css_selector(
                        'a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]')

                    hover = ActionChains(driver).move_to_element(time_post)
                    hover.perform()
                    time.sleep(1)
                    time_full = driver.find_element_by_css_selector(
                        'span[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 tia6h79c fe6kdd0r mau55g9w c8b282yb iv3no6db e9vueds3 j5wam9gi knj5qynh oo9gr5id hzawbc8m"]')
                    print(time_full.text)
                    profile_info.append(time_full.text)
                except:
                    try:
                        print('some error')
                        time_icon = last_post.find_element_by_css_selector(
                            'span[class="tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41"]')
                        prelast_post = driver.find_element_by_xpath(
                            "//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[last()-2]")
                        time_post = prelast_post.find_element_by_css_selector(
                            'a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]')
                        hover = ActionChains(driver).move_to_element(time_post)
                        hover.perform()
                        time.sleep(1)
                        time_full = driver.find_element_by_css_selector(
                            'span[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 tia6h79c fe6kdd0r mau55g9w c8b282yb iv3no6db e9vueds3 j5wam9gi knj5qynh oo9gr5id hzawbc8m"]')
                        print(time_full.text)
                        profile_info.append(time_full.text)
                    except:
                        profile_info.append('')


                # hover = ActionChains(driver).move_to_element(time_icon)
                # hover.perform()
                # time.sleep(1)
                # time_full = driver.find_element_by_css_selector('span[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 tia6h79c fe6kdd0r mau55g9w c8b282yb iv3no6db e9vueds3 j5wam9gi knj5qynh oo9gr5id hzawbc8m"]')

            # time.sleep(2)

        # Парсинг фото профиля
        try:
            print('Ищу фото профиля и кликаю')
            profile_photo = driver.find_element_by_css_selector('div[class="b3onmgus e5nlhep0 ph5uu5jm ecm0bbzt spb7xbtv bkmhp75w emlxlaya s45kfl79 cwj9ozl2"]').click()
            try:
                print('Смотрю нет ли истории')
                time.sleep(3)
                story_or_photo = driver.find_element_by_xpath(".//*[contains(text(), 'Посмотреть фото профиля')]").click()
                time.sleep(3)
                img = driver.find_element_by_css_selector('img[class="ji94ytn4 r9f5tntg d2edcug0"]')
                width = driver.execute_script("return document.getElementsByClassName('ji94ytn4 r9f5tntg d2edcug0')[0].naturalWidth")
                height = driver.execute_script("return document.getElementsByClassName('ji94ytn4 r9f5tntg d2edcug0')[0].naturalHeight")
                print(img.get_attribute('src'))
                profile_info.append(img.get_attribute('src'))
                print(width)
                print(height)
                profile_info.append(str(width) + ' x ' + str(height))
                driver.back()
                time.sleep(2)
            except:
                time.sleep(3)
                img = driver.find_element_by_css_selector('img[class="ji94ytn4 r9f5tntg d2edcug0"]')
                width = driver.execute_script("return document.getElementsByClassName('ji94ytn4 r9f5tntg d2edcug0')[0].naturalWidth")
                height = driver.execute_script("return document.getElementsByClassName('ji94ytn4 r9f5tntg d2edcug0')[0].naturalHeight")
                print(img.get_attribute('src'))
                profile_info.append(img.get_attribute('src'))
                print(width)
                print(height)
                profile_info.append(str(width) + ' x ' + str(height))
                driver.back()
                time.sleep(2)
        except:
            profile_info.append('Нет фото')
            profile_info.append('0х0')

        # Парсинг инфо
        print('Парсинг инфо начал')
        driver.execute_script(f"window.scrollTo(0, 0);")
        time.sleep(2)
        infoblock = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr']/div[@class='tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']/div[@class='cb02d2ww ni8dbmo4 stjgntxs l9j0dhe7 k4urcfbm du4w35lb lzcic4wl']/div[@class='soycq5t1 l9j0dhe7']/div[@class='i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4']/a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 tkr6xdv7 bzsjyuwj cb02d2ww j1lvzwm4'][2]/div[@class='bp9cbjyn rq0escxv j83agx80 pfnyh3mw frgo5egb l9j0dhe7 cb02d2ww hv4rvrfc dati1w0a']")
        infoblock.click()
        time.sleep(3)
        informations = driver.find_element_by_css_selector("div[class='ls2amcm3 pcp91wgn ihqw7lf3 p8fzw8mz discj3wi pfnyh3mw rq0escxv maa8sdkg'")
        infos = informations.find_elements_by_css_selector('div[class="bi6gxh9e"]')
        infos[1].click()
        time.sleep(1)

        # jobs
        parse_info("//div[@class='tu1s4ah4'][1]/div[position()>1]")
        # ihes
        parse_info("//div[@class='tu1s4ah4'][2]/div[position()>1]")
        # schools
        parse_info("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']/div[3]/div[position()>1]")

        infos[2].click()
        time.sleep(1)

        # addresses
        parse_info("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']/div/div[position()>1]")

        infos[3].click()
        time.sleep(1)

        # contacts
        parse_info("//div[@class='tu1s4ah4'][1]/div[@class='oygrvhab']")

        # websites
        parse_info("//div[@class='tu1s4ah4'][2]/div[@class='oygrvhab']")

        # main_info
        try:
            pol = driver.find_element_by_xpath(".//*[contains(text(), 'Пол')]")
            parse_info(".//*[contains(text(), 'Пол')]/../../../../../../../../div[1]")
        except:
            profile_info.append('Not info')
        # birthday_dates
        try:
            date = driver.find_element_by_xpath(".//*[contains(text(), 'Дата рождения')]")
            parse_info("//div[@class='c9zspvje'][2]")
        except:
            profile_info.append('Not data')
        # languages
        try:
            lang = driver.find_element_by_xpath(".//*[contains(text(), 'Языки')]")
            parse_info("//div[3]/div[@class='oygrvhab']")
        except:
            profile_info.append('Not languages')

        infos[4].click()
        time.sleep(2)

        # statuses
        parse_info("//div[1]/div[@class='oygrvhab']")
        # families
        parse_info("//div[2]/div[@class='oygrvhab']")

        infos[5].click()
        time.sleep(1)

        # about_list
        parse_info("//div[1]/div[@class='oygrvhab']")
        # names
        parse_info("//div[2]/div[@class='oygrvhab']")
        # other_names
        parse_info("//div[3]/div[@class='oygrvhab']")
        # quotes
        parse_info("//div[4]/div[@class='oygrvhab']")



        # time.sleep(1)

        # Парсинг кол-во фото
        try:
            print('Ищу Фото')
            fotoblock = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr']/div[@class='tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']/div[@class='cb02d2ww ni8dbmo4 stjgntxs l9j0dhe7 k4urcfbm du4w35lb lzcic4wl']/div[@class='soycq5t1 l9j0dhe7']/div[@class='i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4']/a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 tkr6xdv7 bzsjyuwj cb02d2ww j1lvzwm4'][4]/div[@class='bp9cbjyn rq0escxv j83agx80 pfnyh3mw frgo5egb l9j0dhe7 cb02d2ww hv4rvrfc dati1w0a']")
            fotoblock.click()
        except:
            print('Не нашел, Ищу в Ещё')
            driver.find_element_by_xpath(".//*[contains(text(), 'Ещё')]").click()
            time.sleep(1)
            fotoblock2 = driver.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 oi9244e8 oygrvhab h676nmdw pybr56ya dflh9lhu f10w8fjw scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb'][1]")
            print('Нашел. Жму')
            fotoblock2.click()

        time.sleep(2)
        print('Ищу Альбомы')
        try:
            alboms = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb gderk4og hpfvmrgz dxtxif39 buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[1]//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 tkr6xdv7 bzsjyuwj cb02d2ww j1lvzwm4'][last()]")
            alboms.click()
            time.sleep(1)
            counts = driver.find_elements_by_xpath("//div[@class='rq0escxv rj1gh0hx buofh1pr ni8dbmo4 stjgntxs l9j0dhe7']/div[@class='l9j0dhe7']//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t buofh1pr tgvbjcpo sv5sfqaa obtkqiv7']//div[@class='qzhwtbm6 knvmm38d'][2]")
            a = 0
            hron = []
            for count in counts:
                alb_name = count.find_element_by_xpath('.//..')
                if not 'Фото из хроники' in alb_name.text:
                    ads = (count.text).split(' ')
                    a += int(ads[0])
                    print(a)
                else:
                    ads = (count.text).split(' ')
                    print(ads[0])
                    hron.append(ads[0])

                    print(a)
            profile_info.append(hron)
            profile_info.append(a)

        except:
            print('НЕт фото')
            profile_info.append('[]')
            profile_info.append('0')

        # time.sleep(2)


        # отметки нравится
        likes_list = []
        try:
            driver.find_element_by_xpath(".//*[contains(text(), 'Ещё')]").click()
            time.sleep(2)
            driver.find_element_by_xpath(".//*[contains(text(), 'Отметки \"Нравится\"')]").click()
            time.sleep(1)
            likes = "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 sjgh65i0 hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']"
            scroll_to_down(likes, 0, '')
            likes_sel = driver.find_elements_by_xpath(likes)
            for like in likes_sel:
                print(like.get_attribute('href'))
                like_name = like.find_element_by_xpath(".//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v lrazzd5p oo9gr5id hzawbc8m']")
                print(like_name.text)
                likes_list.append(like_name.text + "----" + like.get_attribute('href'))
        except:
            profile_info.append('0')
        profile_info.append(likes_list)

        # Парсинг друзей
        # time.sleep(3)
        profiles_friends = []
        driver.execute_script(f"window.scrollTo(0, 0);")
        hover = ActionChains(driver).move_to_element(infoblock)
        hover.perform()
        print('Ищу кнопку друзей')
        time.sleep(1)
        friends_btn = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr']/div[@class='tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']/div[@class='cb02d2ww ni8dbmo4 stjgntxs l9j0dhe7 k4urcfbm du4w35lb lzcic4wl']/div[@class='soycq5t1 l9j0dhe7']/div[@class='i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4']/a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 tkr6xdv7 bzsjyuwj cb02d2ww j1lvzwm4'][3]")
        print('Нашел кликаю друзей')

        friends_btn.click()
        time.sleep(2)

        try:
            driver.find_element_by_xpath(".//*[contains(text(), 'Все друзья')]")
            friends = "//div[@class='sjgh65i0'][1]/div/div/div/div[@class='j83agx80 btwxx1t3 lhclo0ds i1fnvgqd']/div[@class='bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr']/div[@class='buofh1pr hv4rvrfc']/div[1]/a"
            scroll_to_down(friends, 0, '')
            friends = driver.find_elements_by_xpath("//div[@class='sjgh65i0'][1]/div/div/div/div[@class='j83agx80 btwxx1t3 lhclo0ds i1fnvgqd']/div[@class='bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr']/div[@class='buofh1pr hv4rvrfc']/div[1]/a")
            for friend in friends:
                print(friend.get_attribute('href'))
                print(friend.text)
                profiles_friends.append(friend.text + "-----" + friend.get_attribute('href'))
        except:
            print('скрытый профиль походу')

        profile_info.append(profiles_friends)
        print(profile_info)

        with open('fb_profile.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(profile_info)
    except Exception as e:
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.3, 400))
        print(e)
        print('какая то ошибка и идем дальше')
        with open('error_p.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(row)


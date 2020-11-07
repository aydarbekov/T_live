# import requests
#
#
# url = 'https://trackensure.com/app/hos/#/eldHOS/viewer/driver/42421/timestamp/1604599199999/timeZone/US%7CCentral'
# a = requests.get(url, auth=('safety.usfreighthaulersinc@gmail.com', '123456789a'))
# print(a.text)
# https://trackensure.com/app/hos/#/eldHOS/viewer/driver/42421/timestamp/1604599199999/timeZone/US%7CCentral
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")
# option.add_argument("--headless")
# option.add_argument("--window-size=1325x744")
# option.add_argument("--remote-debugging-port=9221")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option)


print('Захожу на сайт')
driver.get("https://trackensure.com/login.do")
driver.implicitly_wait(10)

print("Логинюсь")
driver.find_element_by_name('email').send_keys('safety.usfreighthaulersinc@gmail.com')
driver.find_element_by_name('password').send_keys('12345689a')

print("Отправляю форму")
time.sleep(0.2)
driver.find_element_by_css_selector('input[type="submit"]').click()

print("Захожу в эдитор")
driver.get("https://trackensure.com/app/hos/#/eldHOS/editor/driver/56624/timestamp/1604599199999/timeZone/US%7CCentral")
# 56624
# 42421
print('Жду модалки ошибки')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='smooth-hover']")))
try:
    driver.implicitly_wait(0)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'OK')]"))).click()
    driver.implicitly_wait(0)
    print('Дождался и кликнул')
except TimeoutException:
    print('Нет ошибки')
    pass

print("Жму на опен транзакшн")
driver.find_element_by_xpath("//*[contains(text(), 'Open Transaction')]").click()

print('Заполняю форму транзакшна')
driver.find_element_by_xpath("//*[contains(text(), 'Change Driving Duration')]").click()
driver.find_element_by_xpath("//div[@class='row mt-1']/div[@class='col-12 form-group']/textarea[@class='form-control ng-untouched ng-pristine ng-valid']").send_keys('12345689a')

print("Отправляю форму транзакшна")
time.sleep(0.2)
driver.find_element_by_xpath("//*[contains(text(), 'Save')]").click()

print("Жмем на кнопку удаления и ждем пока прогрузит графики")
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[title='Delete']"))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='smooth-hover']")))

print("График догрузился и начинаем удалять ключи:")
print("Находим график и берем оттуда графики дней")
lis = driver.find_element_by_id('eld-graph-events').find_elements_by_tag_name('li')

print("Берем первые 8")
lis = lis[:8]

print("проходим по каждому дню")
to_pass = 0  #определяем переменную по которому будем пропускать уже отмеченные
for li in lis:
    # находим все ключи в одном дне
    keys = li.find_elements_by_css_selector("text[class*='engine-click']")
    print(len(keys))
    print("Проходим по ключам в обратном порядке")
    for key in reversed(keys):
        # условие - если наша переменная равна нулю то кликаем а если больше то пропускаем
        if to_pass == 0:
            print("Кликаю")
            key.click()
            time.sleep(0.5)
            driver.implicitly_wait(0)
            print("пробую найти модалку выбора нескольких ключей")
            try:
                driver.find_element_by_xpath("//div[@class='form-group form-check']/label[@ class ='form-check-label']")
                driver.implicitly_wait(0)
                print("Нашел, считаю сколько ключей можно кликнуть в модалке")
                selects = driver.find_elements_by_xpath(
                    "//div[@class='form-group form-check']/label[@ class ='form-check-label']")
                print("нашел ", len(selects), " и кликаю")
                # к переменной прибавляем кол-во скольких ключей отметили за вычетом одного которого отметили уже
                to_pass += len(selects) - 1
                for select in selects:
                    select.click()
                driver.find_element_by_xpath("//*[contains(text(), 'Close')]").click()
            except:
                print('Ключ один')
                pass
        else:
            print("Уже отмечен иду дальше")
            to_pass -= 1
            continue
driver.find_element_by_xpath("//*[contains(text(), 'Preview')]").click()



# for li in lis:
#     engine_events = li.find_elements_by_css_selector("g[class='engine-events'] > g")
#     print(len(engine_events))
#     print("Проходим по ключам")
#     for key in reversed(keys):
#         checked = key.find_element_by_('text + text')
#         print("Кликаю")
#         key.click()
#         try:
#             print("пробую найти модалку выбора нескольких ключей")
#             selects = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='form-group form-check']/label[@ class ='form-check-label']")))
#             print("нашел и кликаю")
#             for select in selects:
#                 select.click()
#         except TimeoutException:
#             print('Ключ один')
#             continue



import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import random



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

# data = ['4h 48m (14h 04m)|OFF|0%|2020-10-31', '22m|ON|19.202863333333333%|2020-10-31', '52m|D|20.70111111111111%|2020-10-31', '19m|ON|24.226945555555556%|2020-10-31', '1h 30m|D|25.534444444444443%|2020-10-31', '36m|OFF|31.55854111111111%|2020-10-31', '13m|D|34%|2020-10-31', '39m|ON|34.92256777777778%|2020-10-31', '1h 39m|D|37.58888888888889%|2020-10-31', '48m|ON|44.204526666666666%|2020-10-31', '58m|D|47.43333333333333%|2020-10-31', '03m|ON|51.32306444444445%|2020-10-31', '1h 20m|D|51.55555555555556%|2020-10-31', '05m|OFF|56.94709%|2020-10-31', '06m|D|57.31111111111111%|2020-10-31', '16m|ON|57.77273%|2020-10-31', '05m|OFF|58.899254444444445%|2020-10-31', '01m|SB|59.24119888888889%|2020-10-31', '1h 18m|D|59.35444444444445%|2020-10-31', '07m|ON|64.57780666666666%|2020-10-31', '7h 44m (41h 15m)|OFF|65.05889888888889%|2020-10-31', '24h 59m (41h 15m)|OFF|0%|2020-11-01', '8h 31m (41h 15m)|OFF|0%|2020-11-02', '25m|ON|34.076212222222225%|2020-11-02', '34m|D|35.75333333333333%|2020-11-02', '30m|ON|38.075813333333336%|2020-11-02', '2h 14m|D|40.10777777777778%|2020-11-02', '39m|ON|49.095884444444444%|2020-11-02', '13m|D|51.73%|2020-11-02', '32m|OFF|52.59802%|2020-11-02', '30m|D|54.745555555555555%|2020-11-02', '26m|ON|56.788201111111114%|2020-11-02', '1h 50m|D|58.54555555555555%|2020-11-02', '06m|ON|65.93560444444445%|2020-11-02', '2h 40m|D|66.3788888888889%|2020-11-02', '4h 43m (10h 20m)|OFF|77.10287222222222%|2020-11-02', '5h 37m (10h 20m)|OFF|0%|2020-11-03', '25m|ON|22.477834444444444%|2020-11-03', '2h 35m|D|24.21%|2020-11-03', '12m|ON|34.600433333333335%|2020-11-03', '4h 39m|D|35.43222222222222%|2020-11-03', '46m|OFF|54.090645555555554%|2020-11-03', '2h 59m|D|57.2%|2020-11-03', '6h 42m (10h 01m)|OFF|69.13341111111112%|2020-11-03', '3h 19m (10h 01m)|OFF|0%|2020-11-04', '15m|ON|13.266666666666667%|2020-11-04', '58m|D|14.266666666666667%|2020-11-04', '08m|ON|18.198686666666667%|2020-11-04', '1h 57m|D|18.776666666666667%|2020-11-04', '08m|ON|26.597096666666665%|2020-11-04', '33m|D|27.154444444444444%|2020-11-04', '15m|ON|29.378716666666666%|2020-11-04', '46m|D|30.432222222222222%|2020-11-04', '30m|OFF|33.56095555555556%|2020-11-04', '29m|D|35.57666666666667%|2020-11-04', '01m|OFF|37.55789%|2020-11-04', '15m|D|37.67666666666667%|2020-11-04', '06m|ON|38.71236555555556%|2020-11-04', '26m|D|39.154444444444444%|2020-11-04', '05m|ON|40.90877777777778%|2020-11-04', '15m|D|41.297777777777775%|2020-11-04', '13h 24m (44h 19m)|OFF|42.335143333333335%|2020-11-04', '24h 00m (44h 19m)|OFF|0%|2020-11-05', '6h 54m (44h 19m)|OFF|0%|2020-11-06', '25m|ON|27.661091111111112%|2020-11-06', '2h 12m|D|29.33111111111111%|2020-11-06', '4h 31m|ON|38.143165555555555%|2020-11-06', '41m|D|56.24777777777778%|2020-11-06', '09m|ON|59.047292222222225%|2020-11-06', '10m|D|59.69222222222222%|2020-11-06', '1h 04m|ON|60.39556777777778%|2020-11-06', '45m|D|64.71444444444444%|2020-11-06', '35m|ON|67.77164888888889%|2020-11-06', '32m|D|70.12444444444445%|2020-11-06', '02m|ON|72.27952888888889%|2020-11-06', '1h 12m|OFF|72.4732311111111%|2020-11-06', '1h 25m|D|77.28%|2020-11-06', '04m|ON|82.95476222222223%|2020-11-06', '03m|D|83.2688888888889%|2020-11-06', '3h 07m (7h 16m)|SB|83.47435666666667%|2020-11-06', '4h 08m (7h 16m)|SB|0%|2020-11-07']


def all_to_shifts(all_time):
    to_delete = []
    for i in range(len(all_time)-1):
        if '(' in all_time[i]:
            if '(' in all_time[i+1]:
                to_delete.append(i+1)
    for i in reversed(to_delete):
        del all_time[i]
    print(all_time)

    all_shifts = []
    shift = []

    for item in all_time:
        duration, item_type, x1, item_date = item.split('|')
        if '(' in duration:
            half_time, full_time = duration.split('(')
            if 'h' in full_time:
                hour, minute = full_time.split('h')
                hour = int(hour)
                minute = minute.strip(' m)')
            else:
                hour = 0
                minute =  int(full_time.strip(' m)'))
        else:
            if 'h' in duration:
                hour, minute = duration.split('h')
                hour = int(hour)
                minute =    int(minute.strip(' m)'))
            else:
                hour = 0
                minute = int(duration.strip(' m)'))

        duration = f'{hour}:{minute}'
        item_new = f'{duration}|{item_type}|{x1}|{item_date}'

        if (item_type == 'OFF' or item_type == 'SB') and hour >= 10:
            shift.append(item_new)
            all_shifts.append(shift)
            shift = []
            shift.append(item_new)
        else:
            shift.append(item_new)
        print(shift)

    all_shifts.append(shift)
    all_shifts = all_shifts[1:]
    return all_shifts


def analise():
    print("Начинаем сбор данных")
    all_time = []

    for li in reversed(lis):

        li_date = li.get_attribute('data-date')
        lines = li.find_element_by_css_selector("svg[data-graph-mode='identified']").find_element_by_css_selector("g[class='events-durations']").find_elements_by_css_selector("g[class='events'] > g")
        for line in lines:
            line_time = line.find_element_by_tag_name('text')
            # print(line_time.text)
            type_line = line.find_element_by_tag_name('line')
            # print(type_line.get_attribute("class"))
            # print(type_line.get_attribute("x1"))

            if 'event-line-sleep' in type_line.get_attribute("class"):
                type_l = 'SB'
            elif 'event-line-drive' in type_line.get_attribute("class"):
                type_l = 'D'
            elif 'event-line-on' in type_line.get_attribute("class"):
                type_l = 'ON'
            elif 'event-line-off' in type_line.get_attribute("class"):
                type_l = 'OFF'
            line_data = f'{line_time.text}|{type_l}|{type_line.get_attribute("x1")}|{li_date}'
            all_time.append(line_data)
    print(all_time)
    print("Сбор окончен и первичная обработка данных начался")
    shifts = all_to_shifts(all_time)
    return shifts




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
driver.get("https://trackensure.com/app/hos/#/eldHOS/editor/driver/42421/timestamp/1605808799999/timeZone/US%2FCentral")
# 56624
# 42421
print('Жду модалки ошибки')
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='smooth-hover']")))
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
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='smooth-hover']")))

print("График догрузился и начинаем удалять ключи:")
print("Находим график и берем оттуда графики дней")
lis_1 = driver.find_element_by_id('eld-graph-events').find_elements_by_tag_name('li')

print("Берем первые 8")
lis = lis_1[:8]

# УДАЛЕНИЕ УЛЮЧЕЙ
print("проходим по каждому дню")
to_pass = 0  #определяем переменную по которому будем пропускать уже отмеченные
for li in lis:
    # находим все ключи в одном дне
    svgs = li.find_elements_by_css_selector("svg")
    keys = svgs[1].find_elements_by_css_selector("text[class*='engine-click']")
    print(len(keys))
    print("Проходим по ключам в обратном порядке")
    for key in reversed(keys):
        # условие - если наша переменная равна нулю то кликаем а если больше то пропускаем
        if to_pass == 0:
            # print("Кликаю")
            time.sleep(0.5)
            # key.click()
            ActionChains(driver).move_to_element(key).click(key).perform()
            time.sleep(0.5)
            driver.implicitly_wait(0)
            # print("пробую найти модалку выбора нескольких ключей")
            try:
                driver.find_element_by_xpath("//div[@class='form-group form-check']/label[@ class ='form-check-label']")
                driver.implicitly_wait(0)
                # print("Нашел, считаю сколько ключей можно кликнуть в модалке")
                selects = driver.find_elements_by_xpath(
                    "//div[@class='form-group form-check']/label[@ class ='form-check-label']")
                # print("нашел ", len(selects), " и кликаю")
                # к переменной прибавляем кол-во скольких ключей отметили за вычетом одного которого отметили уже
                to_pass += len(selects) - 1
                for select in selects:
                    select.click()
                driver.find_element_by_xpath("//*[contains(text(), 'Close')]").click()
            except:
                # print('Ключ один')
                pass
        else:
            # print("Уже отмечен иду дальше")
            to_pass -= 1
            continue
driver.find_element_by_xpath("//*[contains(text(), 'Preview')]").click()
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='smooth-hover']")))



print("НАЧИНАЕМ СБОР И АНАЛИЗ ДАННЫХ")

shift_btn = driver.find_element_by_css_selector('button[title="Shift"]').click()

while True:
    all_shifts = analise()

    for i in range(len(all_shifts)-1):
        all_drives = 0
        for j in range(len(all_shifts[i])):
            obj = all_shifts[i][j]
            duration, item_type, x1, item_date = obj.split('|')
            hour, minute = duration.split(':')
            all_in_minute = (int(hour) * 60) + int(minute)
            if j == 0:
                print(duration, 'Отдых')
                random_int = random.randint(2, 5)
                if all_in_minute > (600 + random_int) and all_in_minute < 2040:
                    difference = all_in_minute - (600 + random_int)
                    print('двигаем')
                    from_to_btns = driver.find_element_by_css_selector('div[class="bulk-search ng-star-inserted"]').find_elements_by_css_selector('button[class="btn btn-sm btn-default"]')
                    from_to_btns[0].click()
                    time.sleep(2)
                    obj2 = all_shifts[i][j+1]
                    duration2, item_type2, x12, item_date2 = obj2.split('|')
                    day = driver.find_element_by_id('eld-graph-events').find_element_by_css_selector(f'li[data-date="{item_date2}"]')
                    line_to_move = day.find_element_by_css_selector(f"line[x1='{x12}']")
                    print(line_to_move.get_attribute('x2'))
                    # line_to_move.click()
                    print('ПРОБУЮ НАЖАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    ActionChains(driver).move_to_element(line_to_move).click().perform()

                    obj3 = all_shifts[i][-1]
                    duration3, item_type3, x13, item_date3 = obj3.split('|')
                    day = driver.find_element_by_id('eld-graph-events').find_element_by_css_selector(f'li[data-date="{item_date3}"]')
                    line_to_move = day.find_element_by_css_selector(f"line[x1='{x13}']")
                    time.sleep(2)

                    from_to_btns[1].click()
                    time.sleep(2)
                    ActionChains(driver).move_to_element(line_to_move).click().perform()
                    driver.find_element_by_xpath("//*[contains(text(), 'Apply Filter')]").click()
                    time.sleep(1)
                    print(f"Двигаем отдых на {difference // 60} часов и {difference % 60} минут")
                    time_input_hour = driver.find_element_by_xpath("//div[@class='row form-group'][1]/div[@class='col-4']/div/input[@class='form-control form-control-sm ng-untouched ng-pristine ng-valid']")
                    time_input_minute = driver.find_element_by_xpath("//div[@class='row form-group'][2]/div[@class='col-4']/div/input[@class='form-control form-control-sm ng-untouched ng-pristine ng-valid']")

                    time_input_hour.send_keys((difference // 60) * -1)
                    time_input_minute.send_keys((difference % 60) * -1)
                    driver.find_element_by_xpath("//*[contains(text(), 'Preview')]").click()
                    print('вроде двинул')
                    break

                    shift_btn = driver.find_element_by_css_selector('button[title="Shift"]')


                elif all_in_minute > (2040 + random_int):
                    difference = all_in_minute - (2040 + random_int)
                    from_to_btns = driver.find_element_by_css_selector(
                        'div[class="bulk-search ng-star-inserted"]').find_elements_by_css_selector(
                        'button[class="btn btn-sm btn-default"]')
                    from_to_btns[0].click()
                    time.sleep(2)
                    obj2 = all_shifts[i][j + 1]
                    duration2, item_type2, x12, item_date2 = obj2.split('|')
                    day = driver.find_element_by_id('eld-graph-events').find_element_by_css_selector(
                        f'li[data-date="{item_date2}"]')
                    line_to_move = day.find_element_by_css_selector(f"line[x1='{x12}']")
                    print(line_to_move.get_attribute('x2'))
                    # line_to_move.click()
                    print('ПРОБУЮ НАЖАТЬ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    ActionChains(driver).move_to_element(line_to_move).click().perform()

                    obj3 = all_shifts[i][-1]
                    duration3, item_type3, x13, item_date3 = obj3.split('|')
                    day = driver.find_element_by_id('eld-graph-events').find_element_by_css_selector(
                        f'li[data-date="{item_date3}"]')
                    line_to_move = day.find_element_by_css_selector(f"line[x1='{x13}']")
                    time.sleep(2)

                    from_to_btns[1].click()
                    time.sleep(2)

                    ActionChains(driver).move_to_element(line_to_move).click().perform()
                    time.sleep(2)
                    driver.find_element_by_xpath("//*[contains(text(), 'Apply Filter')]").click()

                    print('вроде двинул')
                    break
                    print(f"Двигаем отдых на {difference // 60} часов и {difference % 60} минут")
            else:
                if item_type == 'D':
                    all_drives += all_in_minute
        print(all_drives // 60, ':', all_drives % 60, "общий драйв")
        drive_dif = 660 - all_drives

        print(f"можно добавить {drive_dif // 60} часов и {drive_dif % 60} минут")
        for b in range(len(all_shifts[i+1])):
            obj = all_shifts[i][b]
            duration, item_type, x1, item_date = obj.split('|')
            hour, minute = duration.split(':')
            all_in_minute = (int(hour) * 60) + int(minute)
            if item_type == 'D':
                print('Длинна первого драйва ',  all_in_minute // 60, ':', all_in_minute % 60)
                if all_in_minute <= drive_dif:
                    print("Сдвигаем")
                    can_add = drive_dif - all_in_minute
                    print('остается еще ', can_add // 60, ':', can_add % 60)
                else:
                    break


        print("-------------------------")
        break


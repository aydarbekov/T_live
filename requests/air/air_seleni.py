import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
import datetime
print('Go')

# from crontab import CronTab
# cron = CronTab(user='root')
# job = cron.new(command='echo hello_world')
# job.minute.every(1)
# cron.write()

date = datetime.datetime.now()

with open(f'/home/aza/projects/new/T_live/requests/air/{date} air.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerow(['Название станции', 'US AQI', 'PM2.5', "Погода", "Температура",
                     "Влажность", "Ветер", 'Давление', 'Среднее за день'])

print('Go2')
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--headless")
option.add_argument("--window-size=1325x744")
option.add_argument("--remote-debugging-port=9221")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option)
# driver.maximize_window(driver.window_handles)
# driver.window_handles
print('Захожу на сайт')
driver.get("https://www.iqair.com/kyrgyzstan/bishkek")
driver.implicitly_wait(10)

links = []
links.append("https://www.iqair.com/kyrgyzstan/bishkek")

all_station = driver.find_elements_by_xpath("//li[@class='station-list__item ng-star-inserted']/a")
for station in all_station:
    print(station.get_attribute('href'))
    links.append(station.get_attribute('href'))
    # data.append(station.text)
    # station.click()

for link in links:
    data = []
    driver.get(link)
    time.sleep(2)
    name = link.split('/')
    print(name[-1])
    data.append(name[-1])
    time.sleep(2)
    aqi = driver.find_element_by_xpath("//p[@class='aqi-value__value']")
    print(aqi.text)
    data.append(aqi.text)
    pm = driver.find_element_by_xpath("//table[@class='aqi-overview-detail__other-pollution-table ng-star-inserted']//tr[@class='ng-star-inserted']/td[3]")
    print(pm.text)
    pm_text = pm.text.split(' ')
    print(pm_text[0])
    data.append(pm.text)
    weather = driver.find_element_by_xpath("//div[@class='weather__detail']/table/tbody/tr[1]/td[2]")
    print(weather.text)
    data.append(weather.text)
    temperature = driver.find_element_by_xpath("//div[@class='weather__detail']/table/tbody/tr[2]/td[2]")
    print(temperature.text)
    data.append(temperature.text)
    humidity = driver.find_element_by_xpath("//div[@class='weather__detail']/table/tbody/tr[3]/td[2]")
    print(humidity.text)
    data.append(humidity.text)
    wind = driver.find_element_by_xpath("//div[@class='weather__detail']/table/tbody/tr[4]/td[2]")
    print(wind.text)
    data.append(wind.text)
    pressure = driver.find_element_by_xpath("//div[@class='weather__detail']/table/tbody/tr[5]/td[2]")
    print(pressure.text)
    data.append(pressure.text)
    side_wind = driver.find_element_by_xpath("//tr[@class='today ng-star-inserted']/td[5]/div[@class='wind-section ng-star-inserted']/img")
    average_data = driver.find_element_by_xpath("//tr[@class='today ng-star-inserted']")
    average = average_data.text + '\n' + side_wind.get_attribute('style')
    print(average)
    data.append(average)

    with open(f'/home/aza/projects/new/T_live/requests/air/{date} air.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(data)

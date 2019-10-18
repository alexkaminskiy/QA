from selenium import webdriver
import datetime

actual_day = datetime.datetime.now().day

while True:
    try:
        day = int(input('Enter actual day of the current month and not more than 10 days ahead:'))
    except ValueError:
            print('Enter only integer numbers')
            continue
    if day<actual_day:
        print('Enter actual date')
    elif day > 30:
        print('There are 30 days in current month')
    elif day <= 0:
        print('Date couldn"t be negative or zero')
    elif day > actual_day+9:
        print('Date must be not more than 10 days ahead')
    elif day == '':
        print('Date couldn"t be blanked')
    else:
        break

driver = webdriver.Chrome()
driver.get("https://sinoptik.ua/10-дней")

xpath_max_temperature = '//*[@id="blockDays"]//p[contains(text(),{})]/..//div[@class="temperature"]//div[@class="max"]/span'.format(day)
xpath_min_temperature = '//*[@id="blockDays"]//p[contains(text(),{})]/..//div[@class="temperature"]//div[@class="min"]/span'.format(day)


min_temperature = driver.find_element_by_xpath(xpath_min_temperature).text
max_temperature = driver.find_element_by_xpath(xpath_max_temperature).text
driver.close()
a = 'Temperature in Odessa on the {}:\nMinimum: {}\nMaximum: {}'.format(day, min_temperature, max_temperature)
print(a)
f=open('weather.txt', 'w')
f.write(a)
f.close()

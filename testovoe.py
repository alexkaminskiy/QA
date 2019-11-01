from selenium import webdriver
from time import sleep
import random
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://accounts.ukr.net/login?lang=ru')
driver.maximize_window()

#logging in:
def login():
    user = 'alex_kaminskyi_QA'
    password = 'Alex1987'
    login = driver.find_element_by_id('id-l')
    login.send_keys(user)
    passw = driver.find_element_by_id('id-p')
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/aside/button')))

# generating a random string of letters and digits
def randomStringDigits(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# send mails
def send_mails():
    for i in range(0, 15):
        mail = 'alex_kaminskyi_qa@ukr.net'
        driver.find_element_by_xpath('//*[@id="content"]/aside/button').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="screens"]/div/div/div/button' )))
        driver.find_element_by_xpath('//*[@id="screens"]/div//div[@class="screen__content"]/section/div//div[@style="margin-right: 139px;"]//input[@class="input"]').send_keys(mail)
        driver.find_element_by_xpath('//*[@id="screens"]/div//div[@class="screen__content"]/section//div[@class="sendmsg__form-label"]//div[@class="sendmsg__form-label-field subject"]/input').send_keys(randomStringDigits(10))
        driver.find_element_by_xpath('//*[@frameborder="0"]').send_keys(randomStringDigits(10))
        driver.find_element_by_xpath('//*[@id="screens"]/div/div/div/button').click()
        sleep(1.5)

def varify_mail():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="0"]//span[@class="sidebar__list-link-count"]')))
    count_messages = int(driver.find_element_by_xpath('//*[@id="0"]//span[@class="sidebar__list-link-count"]').text)
    if count_messages == 15:
        print('All {} messages have been received'.format(count_messages))


reseived_messages= {}
def save_messages_to_dict():
    for i in range(0,15):
        driver.find_element_by_xpath('//*[@id="0"]//span[@class="sidebar__list-link-name"]').click()
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="msglist__row unread icon0  ui-draggable"]')))
        driver.find_element_by_xpath('//*[@class="msglist__row unread icon0  ui-draggable"]').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="readmsg"]//div[@class="screen__content"]/h3')))
        theme = driver.find_element_by_xpath('//*[@id="readmsg"]//div[@class="screen__content"]/h3').text
        message = driver.find_element_by_xpath('//*[@id="readmsg"]//div[@class="screen__content"]/section//div[@class="readmsg__content"]/div/span/div/span').text
        reseived_messages.update({theme:message})
        driver.find_element_by_xpath('//*[@id="0"]//span[@class="sidebar__list-link-name"]').click()

def send_data():
    mail = 'alex_kaminskyi_qa@ukr.net'
    driver.find_element_by_xpath('//*[@id="content"]/aside/button').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="screens"]/div/div/div/button')))
    driver.find_element_by_xpath('//*[@id="screens"]/div//div[@class="screen__content"]/section/div//div[@style="margin-right: 139px;"]//input[@class="input"]').send_keys(mail)
    list=[]
    for theme, messages in reseived_messages.items():
        list.append('Received mail on theme {} with message: {}.'.format(theme, messages))
        nums = 0
        letters = 0
        for item in reseived_messages[theme]:
            if item.isnumeric():
                nums += 1
            elif item.isalpha():
                letters += 1
        list.append('It contains {} letter(s) and {} number(s)\n'.format(letters, nums))

    driver.find_element_by_xpath('//*[@frameborder="0"]').send_keys(list)
    driver.find_element_by_xpath('//*[@id="screens"]/div/div/div/button').click()
    print('Message has been sent!')

def delete_messages():
    driver.find_element_by_xpath('//*[@id="0"]/span[@class="sidebar__list-link-name"]').click()
    WebDriverWait(driver, 60).until(
         EC.presence_of_element_located((By.XPATH, '//tr[@class="msglist__row unread icon0  ui-draggable"]//td[@class="msglist__row-address"]/a/span/span')))
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="msglist"]/div/div/div/label/span')))
    driver.find_element_by_xpath('//*[@id="msglist"]/div/div/div/label/span').click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="checkbox noselect"]/input')))
    driver.find_element_by_xpath('//*[@class="checkbox noselect"]/input').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="controls-link remove"]')))
    driver.find_element_by_xpath('//a[@class="controls-link remove"]').click()
    print("Messages have been deleted!")

login()
send_mails()
varify_mail()
save_messages_to_dict()
send_data()
delete_messages()
driver.close()

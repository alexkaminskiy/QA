from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route("/convert_usd_to_uah/", methods = ['POST','GET'])
def convert_usd_to_uah():
    data = request.get_json()
    usd = data['usd']
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, executable_path='C:\\Docs\\chromedriver.exe')
    driver.get('https://finance.i.ua/')
    xpath='//*[@class="table table-data -important"]/thead/../tbody/tr/td/span/span'
    sell_dollar = float(driver.find_element_by_xpath(xpath).text)
    driver.close()
    usd_to_uah = float(usd)*sell_dollar
    return f'{usd_to_uah} UAH'

@app.route("/convert_uah_to_usd/", methods = ['POST','GET'])
def convert_uah_to_usd():
    data=request.get_json()
    uah = data['uah']
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, executable_path='C:\\Docs\\chromedriver.exe')
    driver.get('https://finance.i.ua/')
    xpath = '//*[@class = "table table-data -important"]/thead/../tbody/tr/td[2]/span/span'
    buy_dollar=float(driver.find_element_by_xpath(xpath).text)
    driver.close()
    uah_to_usd=float(uah)/buy_dollar
    return f'{uah_to_usd} USD'

if __name__ == "__main__":
    app.run()

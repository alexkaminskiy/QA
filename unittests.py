import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_money_transfer(self):
        self.driver.get("https://www.portmone.com.ua/r3/uk/p2p-widget/services/card-to-card/index/NovaPoshta")
        actual_result=self.driver.find_element_by_id('bill_amount').get_attribute('placeholder')
        expected_result='від 1 до 25000 грн'

        assert actual_result == expected_result, \
        '\nActual result is: {}\nExpected result is: {}'.format(actual_result,expected_result)

    def test_button(self):
        self.driver.get('http://www.tankathon.com')
        self.driver = WebDriverWait(self.driver, 10).until(
              EC.presence_of_element_located((By.ID, "mock"))
          )
        self.assertTrue(True)

    def test_menu(self):
        self.driver.get('http://www.tankathon.com')
        menu_xpath = '//*[@class="subheader content"]/a'
        list_menu = self.driver.find_elements_by_xpath(menu_xpath)
        new_list=[]
        for item in list_menu:
            new_list.append(item.text)

        menu_more = self.driver.find_element_by_id('more-menu-toggle').text
        new_list.append(menu_more)
        expected_result= ['NBA Home', 'Mock Draft', 'Big Board', 'Compare Prospects', 'Full Order', 'More']
        assert new_list == expected_result,'OMG!!!'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()



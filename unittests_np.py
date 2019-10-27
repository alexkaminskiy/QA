import unittest
from selenium import webdriver

class MyTestNP(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://novaposhta.ua/")

    def test_valid_np_search(self):
        cargo_xpath = "//*[@id='cargo_number']"
        self.driver.find_element_by_xpath(cargo_xpath).send_keys('20450143996902\n')
        actual_result=self.driver.find_element_by_class_name('status').text
        expected_result='Отримано | 17.06.2019 10:10:01'
        assert actual_result == expected_result, \
        '\nActual result is: {}\nExpected result is: {}'.format(actual_result,expected_result)



    def test_invalid_np_search(self):

       cargo_xpath = "//*[@id='cargo_number']"
       self.driver.find_element_by_xpath(cargo_xpath).send_keys('204501439969\n')
       text_xpath="//*[@id='new_track_form']/div[2]/span"
       actual_result=self.driver.find_element_by_xpath(text_xpath).text
       expected_result='Експрес-накладної з таким номером не знайдено.'
       assert actual_result == expected_result, \
           '\nActual result is: {}\nExpected result is: {}'.format(actual_result,expected_result)


    def test_invalid_np_search1(self):

       cargo_xpath = "//*[@id='cargo_number']"
       self.driver.find_element_by_xpath(cargo_xpath).send_keys('456123\n')
       text_xpath="//*[@id='new_track_form']/div[2]/span"
       actual_result=self.driver.find_element_by_xpath(text_xpath).text
       expected_result='Некоректний формат номера накладної. ' \
                       'Номер повинен починатися з цифр 5, 2 або 1 ' \
                       '-переконайтеся в правильності введення номера'
       assert actual_result == expected_result, \
           '\nActual result is: {}\nExpected result is: {}'.format(actual_result,expected_result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()

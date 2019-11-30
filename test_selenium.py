import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get('http://alarab.co.il')

    def test_ramadan_2019_pass(self):
        # validate title is 'مسلسلات رمضان 2019'
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[8]/a').click()
        h1 = self.driver.find_element_by_xpath('//*[@id="left_content"]/div[2]/div[2]/h1')
        self.assertEqual( h1.text, 'مسلسلات رمضان 2019')

    def test_ramadan_2018_nigative(self):
        # validate title is not 'مسلسلات رمضان 2018'
        self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[8]/a').click()
        h1 = self.driver.find_element_by_xpath('//*[@id="left_content"]/div[2]/div[2]/h1')
        self.assertNotEqual(h1.text, 'مسلسلات رمضان 2018')

    def tearDown(self):
        # close the browser window
        self.driver.quit()

        

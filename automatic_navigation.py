import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep


class NavigationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        cls.driver.maximize_window()
        cls.driver.get('http://google.com/')

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        sleep(1)
        driver.forward()
        sleep(1)
        driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
	unittest.main(
		verbosity=2,
		testRunner=HTMLTestRunner(
			output='reportes',
			report_name='automatic-navigation-report'
		)
	)


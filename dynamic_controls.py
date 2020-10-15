import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.maximize_window()
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver
        rmv_checkbox_button = driver.find_element_by_xpath('//*[@id="checkbox-example"]/button')
        rmv_checkbox_button.click()
        WebDriverWait(driver, 15).until(EC.invisibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/div/input'))
        )
        print('Checkbox disappeared.')
        add_checkbox_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[1]/button')
        add_checkbox_button.click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/div[1]/input'))
        )
        print('Checkbox appeared.')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
	unittest.main(
		verbosity=2,
		testRunner=HTMLTestRunner(
			output='reportes',
			report_name='dynamic-controls-report'
		)
	)

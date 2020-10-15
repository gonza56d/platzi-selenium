import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.maximize_window()
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Typos').click()

    def test_find_typo(self):
        driver = self.driver
        paragraph_to_check = driver.find_element_by_xpath('/html/body/div[2]/div/div/p[2]')
        text_to_check = paragraph_to_check.text

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        self.assertEqual(text_to_check, correct_text)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
	unittest.main(
		verbosity=2,
		testRunner=HTMLTestRunner(
			output='reportes',
			report_name='typos-report'
		)
	)

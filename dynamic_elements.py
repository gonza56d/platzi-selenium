import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.maximize_window()
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver
        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()
            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i+1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'Option number {i+1} not found.')
                    tries += 1
                    driver.refresh()

        print(f'Finished in {tries} tries.')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
	unittest.main(
		verbosity=2,
		testRunner=HTMLTestRunner(
			output='reportes',
			report_name='dynamic-elements-report'
		)
	)

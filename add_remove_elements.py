import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from time import sleep


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.maximize_window()
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('How many elements will you add?:'))
        elements_removed = int(input('How many elements will you remove?:'))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(1)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("You're trying to delete more elements that the existent.")
                break

        if total_elements > 0:
            print(f'There are {total_elements} on screen.')
        else:
            print('Tehere are 0 elements.')
        
        sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
	unittest.main(
		verbosity=2,
		testRunner=HTMLTestRunner(
			output='reportes',
			report_name='add-remove-elements-report'
		)
	)


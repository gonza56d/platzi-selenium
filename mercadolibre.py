import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class TestingMercadoLibre(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        cls.driver.maximize_window()
        cls.driver.get('http://mercadolibre.com/')

    def test_search_ps4(self):
        driver = self.driver
        argentina = driver.find_element_by_id('AR')
        argentina.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()

        location = driver.find_element_by_xpath('/html/body/main/div/div[1]/aside/section[2]/dl[12]/dd[6]/a/span[1]')
        location.click()

        order_menu = driver.find_element_by_class_name('ui-dropdown__link')
        order_menu.click()

        order_cheaper = driver.find_element_by_xpath(
            '//*[@id="root-app"]/div/div[1]/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[2]/div/div/a'
        )
        order_cheaper.click()

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(
                f'/html/body/main/div/div[1]/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2/text()'
            )
            article_price = driver.find_element_by_xpath(
                f'/html/body/main/div/div[1]/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]'
            )
            articles.append(article_name)
            prices.append(article_price)

        print(articles, prices)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
	unittest.main(
		verbosity=2,
		testRunner=HTMLTestRunner(
			output='reportes',
			report_name='mercadolibre-report'
		)
	)

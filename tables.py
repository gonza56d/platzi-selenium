import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from prettytable import PrettyTable  # Agregado por mi porque sí


class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.maximize_window()
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        table = PrettyTable()
        driver = self.driver
        _range = 5
        rows = 4
        table_data = [[] for i in range(_range)]
        print('table data: ', table_data)

        for i in range(_range):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)

            for j in range(rows):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)

            # Agregado por mi a PrettyTable para mejor presentacion
            table.add_column(table_data[i][0], [table_data[i][j+1] for j in range(rows-1)])
        
        print('table data: ', table_data)
        print(table)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
	unittest.main(
		verbosity=2,
		testRunner=HTMLTestRunner(
			output='reportes',
			report_name='tables-report'
		)
	)

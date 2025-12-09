from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.demoblaze.com/index.html')

    def click_galaxys6(self):
        card = self.driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        card.click()

    def click_monitor(self):
        monitors_link = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitors_link.click()

    def check_products_counts(self, count):
        monitors_cards = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(monitors_cards) == count


import time
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_card(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxys6()

    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')


def test_count_cards(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    homepage.check_products_counts(2)



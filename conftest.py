import pytest
from urls import URL_MAIN_PAGE
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions




# фикстура запускает браузер FireFox и закрывает его по завершению теста
@pytest.fixture(scope='function')
def driver():
    options = FirefoxOptions()
    driver = Firefox(options=options)
    yield driver
    driver.quit()


# фикстура создаёт объект класса MainPage
# открывает главную страницу и ожидает "кликабельности" кнопки "Заказать" в хедере(как подтверждение загрузки страницы)
@pytest.fixture(scope='function')
def main_page(driver):
    page = MainPage(driver)
    page.open_page(URL_MAIN_PAGE)
    page.wait_for_order_button()
    return page


# фикстура создаёт объект класса OrderPage
# открывает главную страницу и ожидает "кликабельности" кнопки "Заказать" в хедере(как подтверждение загрузки страницы)
@pytest.fixture(scope='function')
def order_page(driver):
    page = OrderPage(driver)
    page.open_page(URL_MAIN_PAGE)
    page.wait_for_order_button()
    return page





import pytest
from data import URL_MAIN_PAGE
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions




# фикстура запускает браузер FireFox и закрывает его по завершению теста
@pytest.fixture(scope='function')
def driver():
    options = FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    driver = Firefox(options=options)
    yield driver
    driver.quit()


# фикстура создаёт объект класса MainPage
# открывает главную страницу и ожидает "кликабельности" кнопки "Заказать" в хедере(как подтверждение загрузки страницы)
@pytest.fixture(scope='function')
def main_page(driver):
    page = MainPage(driver)
    page.open_page(URL_MAIN_PAGE)
    WDW(driver, 5).until(
        EC.element_to_be_clickable(BasePageLocators.BUTTON_ORDER_IN_HEADER_LOCATOR)
    )
    return page


# фикстура создаёт объект класса OrderPage
# открывает главную страницу и ожидает "кликабельности" кнопки "Заказать" в хедере(как подтверждение загрузки страницы)
@pytest.fixture(scope='function')
def order_page(driver):
    page = OrderPage(driver)
    page.open_page(URL_MAIN_PAGE)
    WDW(driver, 5).until(
        EC.element_to_be_clickable(BasePageLocators.BUTTON_ORDER_IN_HEADER_LOCATOR)
    )
    return page





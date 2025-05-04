import allure
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from data import URL_DZEN




# класс содержит базовые методы
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WDW(driver, 10)


    # метод открывает переданную страницу
    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    # метод принимает куки, если сообщение о куки появилось
    @allure.step('Принять куки')
    def accept_cookie(self):
        # ожидание кнопки "да все привыкли"
        try:
            close_cookie = WDW(self.driver, 10).until(
                EC.element_to_be_clickable(BasePageLocators.BUTTON_ACCEPT_COOKIE_LOCATOR)
            )
            close_cookie.click()
        # если кнопка не появилась, то продолжаем тест
        except:
            pass

    # скроллинг до элемента и ожидание его кликабельности
    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(
                EC.element_to_be_clickable(element)
            )
        return element

    # клик по элементу
    @allure.step('Кликнуть элемент')
    def click_to_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    # метод выполняет клик по элементу
    @allure.step('Ожидание видимости элемента')
    def wait_for_element(self, locator):
        return WDW(self.driver, 10).until(
            EC.presence_of_element_located(locator))

    # метод получает текст элемента
    @allure.step('Получить текст')
    def get_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    # метод передаёт тест элементу
    @allure.step('Изменить текст')
    def set_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    # при клике на логотип Яндекс, открывается новая вкладка и в ней открывается страница Дзен
    @allure.step('Проверить переход при клике на логотип Яндекс в хедере')
    @allure.description('При клике на логотип Яндекс, открывается новая вкладка и в ней открывается страница Дзен')
    def click_to_logo_yandex_and_change_to_dzen(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self.wait.until(
            EC.url_contains(URL_DZEN)
        )


    # принятие куки, клик по кнопке "Заказать" в хедере
    @allure.step('Переход в форме заказа при клике кнопки "Заказать" в хедере')
    @allure.description('Принять куки, клик по кнопке "Заказать" в хедере и подтверждение перехода к форме "Заказать"')
    def click_order_button_in_header_and_transition_to_order_page(self):
        self.accept_cookie()
        self.click_to_element(BasePageLocators.BUTTON_ORDER_IN_HEADER_LOCATOR)
        self.wait_for_element(OrderPageLocators.FIELD_INPUT_NAME_LOCATOR)





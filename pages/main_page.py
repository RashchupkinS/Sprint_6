import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage




# класс содержит методы главной страницы и наследует базовые методы
class MainPage(BasePage):

    # Принятие куки, скроллинг и клик по вопросу, проверка наличия ответа
    @allure.step('Клик по вопросу и получение соответствующего ответа')
    @allure.description('Принятие куки, скроллинг и клик по вопросу, проверка наличия ответа')
    def click_to_question_and_get_answer(self, locator_question, locator_answer):
        self.accept_cookie()
        self.scroll_to_element(locator_question)
        self.wait_for_element(locator_question)
        self.click_to_element(locator_question)
        self.wait_for_element(locator_answer)
        return self.driver.find_element(*locator_answer)


    # принятие куки, клик по кнопке "Заказать" в блоке "Как это работает" на главной странице
    @allure.step('Переход в форме заказа при клике кнопки "Заказать" в блоке "Как это работает" на главной странице')
    @allure.description('Принять куки, клик по кнопке "Заказать" в блоке "Как это работает" на главной странице и подтверждение перехода к форме "Заказать"')
    def click_order_button_in_the_middle_of_main_page_and_transition_to_order_page(self):
        self.accept_cookie()
        self.click_to_element(MainPageLocators.BUTTON_ORDER_IN_MIDDLE_LOCATOR)
        self.wait_for_element(OrderPageLocators.FIELD_INPUT_NAME_LOCATOR)





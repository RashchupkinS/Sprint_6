import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators




# класс содержит методы страницы заказа и наследует базовые методы
class OrderPage(BasePage):

    # клик по полю и ввод в него значения
    @allure.title('Клик по полю и его заполнение')
    def fill_text_field(self, locator, text):
        self.click_to_element(locator)
        self.set_text(locator, text)


 # заполнение формы "Для кого самокат"
    @allure.title('Заполнение формы "Для кого самокат"')
    @allure.description('Заполнение полей - "Имя", "Фамилия", "Адрес", "Телефон" и выбор из выпадающего списка станции метро "Охотный ряд"')
    def fill_form_who_is_the_scooter_for(self, user):
        self.fill_text_field(OrderPageLocators.FIELD_INPUT_NAME_LOCATOR, user["name"])
        self.fill_text_field(OrderPageLocators.FIELD_INPUT_SURNAME_LOCATOR, user["surname"])
        self.fill_text_field(OrderPageLocators.FIELD_INPUT_ADDRESS_LOCATOR, user["address"])
        self.click_to_element(OrderPageLocators.FIELD_INPUT_METRO_STATION_LOCATOR)
        self.click_to_element(OrderPageLocators.OHOTNIY_RYAD_METRO_STATION)
        self.fill_text_field(OrderPageLocators.FIELD_INPUT_PHONE_LOCATOR, user["phone"])
        self.click_to_element(OrderPageLocators.BUTTON_NEXT_LOCATOR)


    # заполнение формы "Про аренду"
    @allure.title('Заполнение формы "Про аренду"')
    @allure.description('Заполнение поля - "Комментарий" и выбор "Даты начала аренды" из календаря, "Срока аренды" из выпадающего списка и выбор цвета самоката в чек боксе')
    def fill_form_about_rent(self, user):
        self.click_to_element(OrderPageLocators.FIELD_INPUT_DAY_LOCATOR)
        self.click_to_element(OrderPageLocators.CHOOSE_START_RENT_DAY_LOCATOR)
        self.click_to_element(OrderPageLocators.FIELD_INPUT_RENT_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.CHOOSE_RENT_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.FIELD_INPUT_BLACK_COLOR_LOCATOR)
        self.fill_text_field(OrderPageLocators.FIELD_INPUT_COMMENT_LOCATOR, user["comment"])
        self.click_to_element(OrderPageLocators.BUTTON_MAKE_ORDER_LOCATOR)





import allure
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from data import USER_1, USER_2, URL_DZEN, ORDER_HAS_BEEN_PLACED, URL_MAIN_PAGE




class TestOrderPage:

    @allure.title('Заказ скутера кнопкой "Заказать" в хедере')
    def test_place_order_page_by_click_on_order_button_in_the_header(self, order_page):
        order_page.click_order_button_in_header_and_transition_to_order_page()
        order_page.fill_form_who_is_the_scooter_for(USER_1)
        order_page.fill_form_about_rent(USER_1)
        order_page.click_to_element(OrderPageLocators.BUTTON_YES_LOCATOR)
        confirmation_text = order_page.get_text(OrderPageLocators.WINDOW_WITH_CONFIRMATION_LOCATOR)
        assert ORDER_HAS_BEEN_PLACED in confirmation_text



    @allure.title('Заказ скутера кнопкой "Заказать" в блоке "Как это работает"')
    def test_place_order_page_by_click_on_order_button_in_the_middle_of_main_page(self, main_page, order_page):
        main_page.click_order_button_in_the_middle_of_main_page_and_transition_to_order_page()
        order_page.fill_form_who_is_the_scooter_for(USER_2)
        order_page.fill_form_about_rent(USER_2)
        order_page.click_to_element(OrderPageLocators.BUTTON_YES_LOCATOR)
        confirmation_text = order_page.get_text(OrderPageLocators.WINDOW_WITH_CONFIRMATION_LOCATOR)
        assert ORDER_HAS_BEEN_PLACED in confirmation_text


    @allure.title('Редирект на главную страницу «Самоката», при нажатии на логотип «Самокат» после оформления заказа')
    def test_click_on_the_scooter_logo_after_placing_an_order(self, driver, order_page):
        order_page.click_order_button_in_header_and_transition_to_order_page()
        order_page.fill_form_who_is_the_scooter_for(USER_1)
        order_page.fill_form_about_rent(USER_1)
        order_page.click_to_element(OrderPageLocators.BUTTON_YES_LOCATOR)
        order_page.click_to_element(OrderPageLocators.BUTTON_VIEW_THE_STATUS_LOCATOR)
        order_page.click_to_element(BasePageLocators.LOGO_SCOOTER_LOCATOR)
        assert driver.current_url == URL_MAIN_PAGE


    @allure.title('Редирект в новом окне на главную страницу "Дзен", при нажатии на логотип "Яндекс" после оформления заказа')
    def test_click_on_the_yandex_logo_after_placing_an_order(self, driver, order_page):
        order_page.click_order_button_in_header_and_transition_to_order_page()
        order_page.fill_form_who_is_the_scooter_for(USER_2)
        order_page.fill_form_about_rent(USER_2)
        order_page.click_to_element(OrderPageLocators.BUTTON_YES_LOCATOR)
        order_page.click_to_element(OrderPageLocators.BUTTON_VIEW_THE_STATUS_LOCATOR)
        order_page.click_to_element(BasePageLocators.LOGO_YANDEX_LOCATOR)
        order_page.click_to_logo_yandex_and_change_to_dzen()
        assert driver.current_url == URL_DZEN





from selenium.webdriver.common.by import By




# класс содержит базовые локаторы
class BasePageLocators:

    # кнопка "Заказать" в хедере
    BUTTON_ORDER_IN_HEADER_LOCATOR = By.XPATH, '//button[contains(@class, "Button") and contains(text(), "Заказать")]'
    # кнопка принятия куки - "да все привыкли"
    BUTTON_ACCEPT_COOKIE_LOCATOR = By.ID, "rcc-confirm-button"
    # логотип "Самокат" в хедере
    LOGO_SCOOTER_LOCATOR = By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]'
    # логотип "Яндекс" в хедере
    LOGO_YANDEX_LOCATOR = By.XPATH, '//a[@class ="Header_LogoYandex__3TSOI"]'





from selenium.webdriver.common.by import By
from data import day_str




# класс содержит локаторы страницы "Заказать"
class OrderPageLocators:

    # поле "Имя"
    FIELD_INPUT_NAME_LOCATOR = By.XPATH, "//input[@placeholder='* Имя']"
    # поле "Фамилия"
    FIELD_INPUT_SURNAME_LOCATOR = By.XPATH, "//input[@placeholder='* Фамилия']"
    # поле "Адрес"
    FIELD_INPUT_ADDRESS_LOCATOR = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    # поле "Станция метро"
    FIELD_INPUT_METRO_STATION_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"
    # станция метро "Охотный ряд" из выпадающего списка
    OHOTNIY_RYAD_METRO_STATION = By.XPATH, "//div[@class='Order_Text__2broi' and text()='Охотный Ряд']"
    # поле "Телефон"
    FIELD_INPUT_PHONE_LOCATOR = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    # кнопка "Далее" в форме заказа
    BUTTON_NEXT_LOCATOR = By.XPATH, '//button[@class ="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Далее")]'


    # поле "Когда привезти самокат"
    FIELD_INPUT_DAY_LOCATOR = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    # выбор даты когда привезти самокат из выпадающего календаря
    CHOOSE_START_RENT_DAY_LOCATOR = By.XPATH, f"//div[contains(@aria-label, '{day_str}-е мая 2025')]"
    # поле "Срок аренды"
    FIELD_INPUT_RENT_PERIOD_LOCATOR = By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and text()='* Срок аренды']"
    # выбор срока аренды из выпадающего списка
    CHOOSE_RENT_PERIOD_LOCATOR = By.XPATH, ".//div[text()='трое суток']"
    # выбор цвета самоката "чёрный жемчуг"
    FIELD_INPUT_BLACK_COLOR_LOCATOR = By.ID, "black"
    # поле "Комментарий"
    FIELD_INPUT_COMMENT_LOCATOR = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    # кнопка "Заказать" на главной страницу, в блоке заказа
    BUTTON_MAKE_ORDER_LOCATOR = By.XPATH, '//button[@class ="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Заказать")]'


    # кнопка "Да" в окне "Хотите оформить заказ"
    BUTTON_YES_LOCATOR = By.XPATH, '//button[@class ="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Да")]'


    # окно "Заказ оформлен"
    WINDOW_WITH_CONFIRMATION_LOCATOR = By.XPATH, ".//div[text()='Заказ оформлен']"
    # кнопка "Посмотреть статус" в окне "Заказ оформлен"
    BUTTON_VIEW_THE_STATUS_LOCATOR = By.XPATH, '//button[@class ="Button_Button__ra12g Button_Middle__1CSJM" and contains(text(), "Посмотреть статус")]'





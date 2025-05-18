from selenium.webdriver.common.by import By




# класс содержит локаторы главной страницы
class MainPageLocators:

    # вопрос - "Сколько это стоит? И как оплатить?"
    QUESTION_1_LOCATOR = By.ID, "accordion__heading-0"
    # вопрос - "Хочу сразу несколько самокатов! Так можно?"
    QUESTION_2_LOCATOR = By.ID, "accordion__heading-1"
    # вопрос - "Как рассчитывается время аренды?"
    QUESTION_3_LOCATOR = By.ID, "accordion__heading-2"
    # вопрос - "Можно ли заказать самокат прямо на сегодня?"
    QUESTION_4_LOCATOR = By.ID, "accordion__heading-3"
    # вопрос - "Можно ли продлить заказ или вернуть самокат раньше?"
    QUESTION_5_LOCATOR = By.ID, "accordion__heading-4"
    # вопрос - "Вы привозите зарядку вместе с самокатом?"
    QUESTION_6_LOCATOR = By.ID, "accordion__heading-5"
    # вопрос - "Можно ли отменить заказ?"
    QUESTION_7_LOCATOR = By.ID, "accordion__heading-6"
    # вопрос - "Я жизу за МКАДом, привезёте?
    QUESTION_8_LOCATOR = By.ID, "accordion__heading-7"

    # ОТВЕТ на вопрос - "Сколько это стоит? И как оплатить?"
    ANSWER_1_LOCATOR = By.ID, "accordion__panel-0"
    # ОТВЕТ на вопрос - "Хочу сразу несколько самокатов! Так можно?"
    ANSWER_2_LOCATOR = By.ID, "accordion__panel-1"
    # ОТВЕТ на вопрос - "Как рассчитывается время аренды?"
    ANSWER_3_LOCATOR = By.ID, "accordion__panel-2"
    # ОТВЕТ на вопрос - "Можно ли заказать самокат прямо на сегодня?"
    ANSWER_4_LOCATOR = By.ID, "accordion__panel-3"
    # ОТВЕТ на вопрос - "Можно ли продлить заказ или вернуть самокат раньше?"
    ANSWER_5_LOCATOR = By.ID, "accordion__panel-4"
    # ОТВЕТ на вопрос - "Вы привозите зарядку вместе с самокатом?"
    ANSWER_6_LOCATOR = By.ID, "accordion__panel-5"
    # ОТВЕТ на вопрос - "Можно ли отменить заказ?"
    ANSWER_7_LOCATOR = By.ID, "accordion__panel-6"
    # ОТВЕТ на вопрос - "Я жизу за МКАДом, привезёте?
    ANSWER_8_LOCATOR = By.ID, "accordion__panel-7"

    # кнопка "Заказать" в блоке "Как это работает"
    BUTTON_ORDER_IN_MIDDLE_LOCATOR = By.XPATH, '//button[contains(@class, "Button_Middle") and contains(text(), "Заказать")]'





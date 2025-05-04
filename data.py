from locators.main_page_locators import MainPageLocators
from datetime import datetime, timedelta




# Главная страница "Яндекс.Самокат"
URL_MAIN_PAGE = "https://qa-scooter.praktikum-services.ru/"

# Страница "Заказать"
URL_ORDER_PAGE = URL_MAIN_PAGE + "order"

# Страница "Дзен"
URL_DZEN = "https://dzen.ru/?yredirect=true"

# Текст ответов на вопросы в блоке "Вопросы о важном"
# ОТВЕТ на вопрос - "Сколько это стоит? И как оплатить?"
TEXT_ANSWER_1 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
# ОТВЕТ на вопрос - "Хочу сразу несколько самокатов! Так можно?"
TEXT_ANSWER_2 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
# ОТВЕТ на вопрос - "Как рассчитывается время аренды?"
TEXT_ANSWER_3 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
# ОТВЕТ на вопрос - "Можно ли заказать самокат прямо на сегодня?"
TEXT_ANSWER_4 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
# ОТВЕТ на вопрос - "Можно ли продлить заказ или вернуть самокат раньше?"
TEXT_ANSWER_5 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
# ОТВЕТ на вопрос - "Вы привозите зарядку вместе с самокатом?"
TEXT_ANSWER_6 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
# ОТВЕТ на вопрос - "Можно ли отменить заказ?"
TEXT_ANSWER_7 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
# ОТВЕТ на вопрос - "Я жизу за МКАДом, привезёте?
TEXT_ANSWER_8 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."

# переменная содержит список с параметризованными данными, применяемыми в блоке "Вопросы о важном"
# локатор вопроса, локатор ответа и корректный текст ответа на вопрос
correct_answers_to_the_questions = [
            (MainPageLocators.QUESTION_1_LOCATOR, MainPageLocators.ANSWER_1_LOCATOR, TEXT_ANSWER_1),
            (MainPageLocators.QUESTION_2_LOCATOR, MainPageLocators.ANSWER_2_LOCATOR, TEXT_ANSWER_2),
            (MainPageLocators.QUESTION_3_LOCATOR, MainPageLocators.ANSWER_3_LOCATOR, TEXT_ANSWER_3),
            (MainPageLocators.QUESTION_4_LOCATOR, MainPageLocators.ANSWER_4_LOCATOR, TEXT_ANSWER_4),
            (MainPageLocators.QUESTION_5_LOCATOR, MainPageLocators.ANSWER_5_LOCATOR, TEXT_ANSWER_5),
            (MainPageLocators.QUESTION_6_LOCATOR, MainPageLocators.ANSWER_6_LOCATOR, TEXT_ANSWER_6),
            (MainPageLocators.QUESTION_7_LOCATOR, MainPageLocators.ANSWER_7_LOCATOR, TEXT_ANSWER_7),
            (MainPageLocators.QUESTION_8_LOCATOR, MainPageLocators.ANSWER_8_LOCATOR, TEXT_ANSWER_8),
]

# тестовые данные пользователя 1
USER_1 = {
    "name": "Кузьма",
    "surname": "Минин",
    "address": "Москва, Красная площадь",
    "phone": "+79991112233",
    "comment": "Поспешай друже"
}

# тестовые данные пользователя 2
USER_2 = {
    "name": "Дмитрий",
    "surname": "Пожарский",
    "address": "Москва, Красная площадь",
    "phone": "+79993332211",
    "comment": "Не спеши друже"
}


# проверка оформления заказа
ORDER_HAS_BEEN_PLACED = "Заказ оформлен"


# дата заказа самоката форматируется как "текущее число + 2 дня"
order_date = datetime.now() + timedelta(days=2)
day_str = f"{order_date.day}"




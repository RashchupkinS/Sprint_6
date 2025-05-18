import allure
import pytest
from data import correct_answers_to_the_questions




class TestMainPage:

    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text", correct_answers_to_the_questions)
    @allure.title('Проверка списка в разделе "Вопросы о важном"')
    @allure.description('Поиск вопроса на главной странице, в блоке "Вопросы о важном". При клике на вопрос открывается ответ. Тест проверяет текст ответа с требуемым')
    def test_check_drop_down_list_with_questions(self, main_page, question_locator, answer_locator, expected_text):
        text_answer = main_page.click_to_question_and_get_answer(question_locator, answer_locator)
        assert text_answer.text == expected_text





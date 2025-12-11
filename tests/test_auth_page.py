from conftest import driver
from pages.auth_page import AuthPage
from time import sleep

"""Позитивные функциональные тесты"""

"""1. Страница "Вход по временному коду" загружена"""
def test_login_form_is_loaded(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    assert "Вход по временному коду" in ap.get_title_text()

"""2. Поле "E-mail или мобильный телефон" отображается"""
def test_email_or_phone_field_is_displayed(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    assert ap.email_or_phone_field_is_displayed()

"""3. Кнопка "Получить код" отображается"""
def test_get_code_button_is_displayed(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    assert ap.get_code_button_is_displayed()

"""4. Кнопка "Войти со своим паролем" отображается"""
def test_login_with_password_btn_is_displayed(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    assert ap.login_with_password_btn_is_displayed()

"""5. Заголовок "войти другим способом" отображается"""
def test_login_other_way_title_is_displayed(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    assert ap.login_other_way_title_is_displayed()

"""6. Ссылка на пользовательское соглашение отображается"""
def test_user_agreement_link_is_displayed(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    assert ap.user_agreement_link_is_displayed()

"""7. Ссылка на раздел "Помощь" отображается"""
def test_help_link_is_displayed(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    assert ap.help_link_is_displayed()

"""8. Кнопка "Получить код" доступна для нажатия с валидным email"""
def test_button_enabled_with_valid_email(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.enter_email("test@gmail.ru")
    sleep(5)
    assert ap.is_get_code_button_enabled()

"""9. Кнопка "Получить код" доступна для нажатия с валидным телефоном"""
def test_button_enabled_with_valid_phone(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.enter_phone("+79987654321")
    sleep(5)
    assert ap.is_get_code_button_enabled()

"""10. Ввод валидного email """
def test_successful_code_email(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.enter_email("test@gmail.ru")
    ap.click_get_code()
    sleep(30) #Ввести капчу
    assert "Код подтверждения отправлен на адрес\ntest@gmail.ru" in ap.get_success_message()

"""11. Ввод валидного телефона 12 цифр"""
def test_successful_code_phone(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.enter_phone("+79987654321")
    ap.click_get_code()
    sleep(30) #Ввести капчу
    assert "Код подтверждения отправлен на номер\n+7 998 765-43-21" in ap.get_success_message()

"""12. Переход на страницу пользовательского соглашения"""
def test_text_agreement_is_loaded(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.user_agreement_text_is_loaded()
    expected_url = "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
    current_url = driver.current_url
    assert current_url == expected_url

"""13. Переход на страницу раздела "Помощь" """
def test_help_content_is_loaded(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    assert ap.help_content_is_loaded()

"""14. Загрузка формы входа в ЛК с паролем"""
def test_load_login_with_password_link(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.click_login_with_password_link()
    sleep(5)
    assert ap.password_field_is_displayed()


"""Негативные тесты"""

"""15. Ввод email некорректной формы"""
def test_error_invalid_email(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.enter_email("invalid@")
    sleep(5)
    ap.click_get_code()
    assert ("Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX,"
            " или email в формате example@email.ru") in ap.get_error_message()

"""16. Ввод email кириллическими буквами"""
def test_error_invalid_email(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.enter_email("ыыы@ффф.ру")
    sleep(5)
    ap.click_get_code()
    assert ("Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX,"
            " или email в формате example@email.ru") in ap.get_error_message()

"""17. Ввод невалидного телефона - 10 цифр"""
def test_error_invalid_phone(driver):
    ap = AuthPage(driver)
    ap.open()
    ap.enter_phone("+7998765432")
    ap.click_get_code()
    sleep(5)
    assert ("Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX,"
            " или email в формате example@email.ru") in ap.get_error_message()

"""18. Ввод невалидного телефона - 12 цифр"""
def test_error_invalid_phone(driver):
    ap = AuthPage(driver)
    ap.open()
    ap.enter_phone("+799876543210")
    ap.click_get_code()
    sleep(5)
    assert ("Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX,"
            " или email в формате example@email.ru") in ap.get_error_message()

"""19. Ввод в поле "E-mail или мобильный телефон" пробела"""
def test_get_code_button_disabled_when_empty(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.enter_email("")
    sleep(5)
    assert ("Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX,"
            " или email в формате example@email.ru") in ap.get_error_message()

"""20. Ввод невалидного лицевого счета 11 цифр """
def test_error_invalid_account(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.click_login_with_password_link()
    sleep(5)
    ap.enter_account("11111111111", "Q!2312")
    ap.click_enter()
    sleep(30) #Ввести капчу
    assert ap.get_error_message_acc()

"""21. Ввод несуществующего лицевого счета 12 цифр"""
def test_error_wrong_account(driver):
    ap = AuthPage(driver)
    ap.open()
    sleep(7)
    ap.click_login_with_password_link()
    sleep(5)
    ap.enter_account("111111111111", "Q!2312")
    ap.click_enter()
    sleep(30) #Ввести капчу
    assert ap.get_error_message_wracc()

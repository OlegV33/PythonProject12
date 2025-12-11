from selenium.webdriver.common.by import By
from time import sleep

class AuthPage:
    URL = "https://lk.rt.ru/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_title_text(self):
        return self.driver.find_element(By.TAG_NAME, "h1").text

    def email_or_phone_field_is_displayed(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"address\"]').is_displayed()

    def get_code_button_is_displayed(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"otp_get_code\"]').is_displayed()

    def is_get_code_button_enabled(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"otp_get_code\"]').is_enabled()

    def is_get_code_button_disabled(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"otp_get_code\"]').is_disabled()

    def login_with_password_btn_is_displayed(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"standard_auth_btn\"]').is_displayed()

    def login_other_way_title_is_displayed(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/div[4]/div[1]/span[2]').is_displayed()

    def user_agreement_link_is_displayed(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"rt-auth-agreement-link\"]').is_displayed()

    def user_agreement_text_is_loaded(self):
        self.driver.find_element(By.XPATH, '//*[@id=\"rt-auth-agreement-link\"]').click()
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(5)

    def help_link_is_displayed(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"faq-open\"]/a').is_displayed()

    def help_content_is_loaded(self):
        self.driver.find_element(By.XPATH, '//*[@id=\"faq-open\"]/a').click()
        sleep(5)
        return self.driver.find_element(By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/div/div/h1').is_displayed()

    def password_field_is_displayed(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"password\"]').is_displayed()

    def enter_email(self, email):
        field = self.driver.find_element(By.XPATH, '//*[@id=\"address\"]')
        field.clear()
        field.send_keys(email)

    def enter_phone(self, phone):
        field = self.driver.find_element(By.XPATH, '//*[@id=\"address\"]')
        field.clear()
        field.send_keys(phone)

    def click_get_code(self):
        self.driver.find_element(By.XPATH, '//*[@id=\"otp_get_code\"]').click()

    def click_login_with_password_link(self):
        self.driver.find_element(By.XPATH, '//*[@id=\"standard_auth_btn\"]').click()

    def get_text(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"otp-code-form-description\"]').text

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"address-meta\"]').text

    def get_success_message(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"otp-code-form-description\"]').text

    def enter_account(self, account, password):
        self.driver.find_element(By.XPATH, '//*[@id=\"t-btn-tab-ls\"]').click()
        acc = self.driver.find_element(By.XPATH, '//*[@id=\"username\"]')
        pas = self.driver.find_element(By.XPATH, '//*[@id=\"password\"]')
        acc.clear()
        pas.clear()
        acc.send_keys(account)
        pas.send_keys(password)

    def click_enter(self):
        self.driver.find_element(By.XPATH, '//*[@id=\"kc-login\"]').click()

    def get_error_message_acc(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"username-meta\"]').is_displayed()

    def get_error_message_wracc(self):
        return self.driver.find_element(By.XPATH, '//*[@id=\"form-error-message\"]').is_displayed()


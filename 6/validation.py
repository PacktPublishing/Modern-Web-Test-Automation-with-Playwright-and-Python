from playwright.sync_api import expect

from pages.base_page import BasePage
from utils.utils import take_screenshot, log_message, LogLevel


class AppValidation(BasePage):
    def __init__(self, setup_all_pages):
        self.login_page, self.main_page = setup_all_pages
        super().__init__(self.login_page)


    def validate_logged_in(self):
        login_button = self.login_page.login_button
        try:
            expect(login_button).to_be_hidden()
        except:
            log_message(self.logger,"login failed", LogLevel.ERROR)
            take_screenshot("login failed")
            raise "Login failed"


    def validate_failed_login(self, expected_error):
        login_button = self.login_page.login_button
        try:
            expect(login_button).to_be()

        except:
            log_message(self.logger,"login button failed to be visible", LogLevel.ERROR)
            take_screenshot("login button failed to be visible")
            raise "expected login button to be visible but it was displayed"




        error_message = self.login_page.get_error_message(message_error)
        expect(error_message).to_be_visible(), "login button was expected to be hidden, but it was visible"


        self.error_message = self.page.locator("//div[@id='email_container']")


    def get_error_message(self, message_error):
        return self.error_message.locator(f"//div[contains(text(), '{message_error}')]")
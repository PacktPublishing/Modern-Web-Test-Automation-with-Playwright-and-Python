import pytest

from utils.config import VALID_CREDENTIALS
from utils.validation import AppValidation


def test_successfully_login(setup_login_page,validation):
    login_page = setup_login_page
    main_page = login_page.perform_login(VALID_CREDENTIALS["email"],VALID_CREDENTIALS["password"])
    assert main_page is not None, "Login failed unexpectedly!"

    validation.validate_logged_in()



@pytest.mark.parametrize(
    "email, password, expected_error",
    [
        ("wrong_email_template","valid_password","error"),
        ("valid_email@gmail.com","wrong_password","error")

    ],
)
def test_invalid_login_and_verify_error_message(setup_login_page,validation,email, password, expected_error):
    login_page = setup_login_page
    main_page = login_page.perform_login(email, password)

    assert main_page is None, "Login should have failed but it passed!"
    validation.validate_failed_login(expected_error)


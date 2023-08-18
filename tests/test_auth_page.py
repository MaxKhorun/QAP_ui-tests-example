from pages.auth_page import AuthPage
from settings import login_email, login_passw


def test_authorisation(web_browser):

    page = AuthPage(web_browser)
    page.email.send_keys(login_email)
    page.password.send_keys(login_passw)
    page.btn.click()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

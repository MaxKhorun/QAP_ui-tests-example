from pages.auth_page import AuthPage
from settings import login_email, login_passw


def test_authorisation(web_browser):

    page = AuthPage(web_browser)
    page.email.send_keys('maxim@mail.ru')
    page.password.send_keys('1234')
    page.btn.click()

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

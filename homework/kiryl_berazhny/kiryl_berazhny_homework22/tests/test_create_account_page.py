from pages.create_account_page import CreateAccountPage as CAP
from pages.confirm_page import ConfirmPage as CP
import random


def test_strong_password(driver):  # проверяем подсвечен ли показатель надежности пароля
    ca_page = CAP(driver)
    ca_page.open_page()
    ca_page.scroll()
    ca_page.enter_pass_one('Qwertyasd8')
    assert ca_page.check_password.is_displayed()


def test_confirm_text(driver):  # проверяем, правильно ли приняты данные для регистрации аккаунта
    ca_page = CAP(driver)
    ca_page.open_page()
    first_name = 'Kiryl'
    ca_page.enter_first_name(first_name)
    second_name = 'Berazhny'
    ca_page.enter_second_name(second_name)
    ca_page.scroll()
    email = f'q@{str(random.randint(1, 99999))}.com'  # так как нельзя одну и ту же почту
    ca_page.enter_email(email)
    ca_page.enter_pass_one('Qwertyasd8')
    ca_page.enter_pass_two('Qwertyasd8')
    ca_page.click_submit()
    conf_page = CP(driver)
    assert f'{first_name} {second_name}\n{email}' == conf_page.check_result


def test_existing_email(driver):  # проверяем, подсвечена ли ошибка при регистрации существующей почты
    ca_page = CAP(driver)
    ca_page.open_page()
    ca_page.enter_first_name('Kiryl')
    ca_page.enter_second_name('Berazhny')
    ca_page.scroll()
    email = f'q@{str(random.randint(1, 99999))}.com'  # так как нельзя одну и ту же почту
    ca_page.enter_email(email)
    ca_page.enter_pass_one('Qwertyasd8')
    ca_page.enter_pass_two('Qwertyasd8')
    ca_page.click_submit()
    conf_page = CP(driver)
    conf_page.click_select_out()
    conf_page.click_sign_out()
    ca_page.open_page()
    ca_page.enter_first_name('Kiryl')
    ca_page.enter_second_name('Berazhny')
    ca_page.scroll()
    ca_page.enter_email(email)
    ca_page.enter_pass_one('Qwertyasd8')
    ca_page.enter_pass_two('Qwertyasd8')
    ca_page.click_submit()
    assert ca_page.error_text.is_displayed()

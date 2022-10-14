from Src.PageObject.Pages.LoginPage import LoginUser
from time import sleep

def login_user(driver, username, password):
    login = LoginUser(driver)

    login.login_user_name.send_keys(username)
    sleep(1)
    login.login_password.send_keys(password)
    sleep(1)
    login.login_button.click()
    sleep(5)
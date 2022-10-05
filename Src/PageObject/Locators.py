# The intent is to test login functionality on Booking
# The user has already registered on Bookig
# Step 1 - Open https://www.booking.com/
# Step 2 - Locate the Login Button and Sign-In using Credentials
class Locator(object):
    # locators for booking homepage
    # book_decline_cookies = '//*[@id="onetrust-accept-btn-handler"]'
    home_login = '//*[@id="loginSignup"]/li[1]/a'
    home_signup = '//*[@id="loginSignup"]/li[2]/a'

    # locators for login page
    login_user_name = '//*[@id="inputEmail"]'
    login_password = '//*[@id="inputPassword"]'
    login_button = '//*[@id="login"]'

    login_captcha = '//*[@id="recaptcha-anchor"]/div[1]'
    login_captcha_iframe = '//*[@id="#divDynamicRecaptcha1"]/div/div/iframe'


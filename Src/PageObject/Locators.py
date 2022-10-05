# The intent is to test login functionality on Booking
# The user has already registered on Bookig
# Step 1 - Open https://www.booking.com/
# Step 2 - Locate the Login Button and Sign-In using Credentials
class Locator(object):
    # locators for booking homepage
    book_decline_cookies = '//*[@id="onetrust-accept-btn-handler"]'
    book_login = '//*[@id="b2indexPage"]/header/nav[1]/div[2]/div[6]/a'
    book_signup = '//*[@id="b2indexPage"]/header/nav[1]/div[2]/div[5]/a'

    # locators for login page
    book_login_user_name = '//*[@id="username"]'
    book_login_user_button = '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/button'
    book_login_password = '//*[@id="password"]'
    book_login_password_button = '//*[@id="root"]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/button/span'



from selenium.webdriver.common.by import By

base_url = "https://www.saucedemo.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.xpath_image_login = '//*[@id="root"]/div/div[2]/div[1]/div[2]'
        self.input_user = 'user-name'
        self.input_password = 'password'
        self.button = 'login-button'
        self.xpath_page_init = '//*[@id="header_container"]/div[2]/span'
        self.xpath_loginerror = '//*[@id="login_button_container"]/div/form/div[3]'
        self.xpath_loginsucced = '//*[@id="inventory_container"]/div/div[2]/div[2]/div[1]/div'
    def get_page_login(self):
        return self.driver.find_element(By.ID, self.button)

    def get_input_user(self):
        return self.driver.find_element(By.ID, self.input_user)

    def get_input_password(self):
        return self.driver.find_element(By.ID, self.input_password)

    def send_text_user(self, user):
        self.get_input_user().send_keys(user)

    def send_password(self, password):
        self.get_input_password().send_keys(password)

    def view_page(self):
        return self.get_page_login().is_displayed()

    def click_element(self):
        self.get_page_login().click()

    def get_error(self):
        return self.driver.find_element(By.XPATH, self.xpath_loginerror)

    def view_error(self):
        return self.get_error().is_displayed()

    def clear_user_field(self):
        user_field = self.driver.find_element(By.ID, self.input_user)
        user_field.clear()

    def clear_password_field(self):
        password_field = self.driver.find_element(By.ID, self.input_password)
        password_field.clear()

    def get_suced(self):
        return self.driver.find_element(By.XPATH, self.xpath_loginsucced)

    def view_suced(self):
        return self.get_suced().is_displayed()
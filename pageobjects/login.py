from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button"
    link_logout_linktext = "Logout"

    def __init__(self, driver) -> None:
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, Login.textbox_username_id).clear()
        self.driver.find_element(
            By.ID, Login.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, Login.textbox_password_id).clear()
        self.driver.find_element(
            By.ID, Login.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, Login.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(
            By.LINK_TEXT, Login.link_logout_linktext).click()

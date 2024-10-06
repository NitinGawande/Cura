from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    link_siteclick_xpath="//a[@id='btn-make-appointment']"
    textbox_username_name="username"
    textbox_password_name="password"
    button_login_xpath="//button[@id='btn-login']"


    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait

    def clickfirst(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@id='btn-make-appointment']"))).click()

    def SetUserName(self,username):
        self.wait.until(EC.element_to_be_clickable((By.NAME, "username"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "username"))).clear()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys(username)

    def SetPassword(self,password):
        self.wait.until(EC.element_to_be_clickable((By.NAME,"password"))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME,"password"))).clear()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(password)

    def Clicklogin(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='btn-login']"))).click()



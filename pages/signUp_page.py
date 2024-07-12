import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class tashkeel:
    def __init__(self, driver):
        self.driver = driver

    signin_btn = '//*[@id="root"]/div[1]/div/header/nav/div[2]/button[2]'
    signup_btn = 'a[class="underline mx-[4px] text-tashkeel_primary"]'
    name = 'input[type="text"]'
    email = 'input[type="email"]'
    password = 'input[type="password"]'
    confirm_password = '//*[@id=":ra:-form-item"]/input'
    create_btn = '//*[@id="root"]/div[1]/div/div[3]/form/div[2]/button'

    def signup(self, Name, Email, Password, confirm_password):

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[1]/div/header/nav/div[2]/button[2]'))).click()
        self.driver.find_element(By.CSS_SELECTOR, self.signup_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, self.name).send_keys(Name)
        self.driver.find_element(By.CSS_SELECTOR, self.email).send_keys(Email)
        self.driver.find_element(By.CSS_SELECTOR, self.password).send_keys(Password)
        self.driver.find_element(By.XPATH, self.confirm_password).send_keys(confirm_password)
        self.driver.find_element(By.XPATH, self.create_btn).click()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)
        time.sleep(2)

    def validsignup(self):
        try:
            return self.driver.find_element(By.XPATH,
                                            '//*[@id="root"]/div[1]/div/div[3]/div/div/h3').text
        except NoSuchElementException:
            return False, "Failed to locate message element"

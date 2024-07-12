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
    email = 'input[type="email"]'
    password = 'input[type="password"]'
    create_btn = 'button[class="inline-flex items-center justify-center whitespace-nowrap font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 h-10 px-4 bg-tashkeel_primary border-tashkeel_primary text-white hover:bg-tashkeel_primary_hover hover:border-tashkeel_primary_hover text-[1.4rem] md:text-[1.6rem] py-2 w-full rounded-[5px] md:py-6 disabled:bg-[#c4c4c4] disabled:border-[#c4c4c4] disabled:cursor-not-allowed"]'

    def signin(self, Email, Password):

        # wait = WebDriverWait(self.driver, 5)
        # wait.until(EC.presence_of_element_located(
        #     (By.XPATH, '//*[@id="root"]/div[1]/div/header/nav/div[2]/button[2]'))).click()
        # self.driver.find_element(By.XPATH, self.signin_btn).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.email))).send_keys(Email)
        self.driver.find_element(By.CSS_SELECTOR, self.password).send_keys(Password)
        self.driver.find_element(By.CSS_SELECTOR, self.create_btn).click()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)
        time.sleep(2)

    def validsignIn(self):
        try:
            return self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/header/nav/div[2]/div[2]/div/div').is_displayed()
        except NoSuchElementException:
            return False, "Failed to locate message element"

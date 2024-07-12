import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import tashkeel

class tashkeel1:
    def __init__(self, driver):
        self.driver = driver
        self.loginpage = tashkeel(driver)

    larger_files_btn = '//*[@id="root"]/div[1]/div/header/nav/div[2]/button/span/span'
    more_btn= '//*[@id="root"]/div[1]/div/div[3]/div[2]/button[1]'
    number = 'input[type="tel"]'

    radio_btn1 = ('//*[@class="aspect-square h-4 w-4 rounded-full border-2 justify-center p-2 text-primary shadow '
                  'focus:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed '
                  'disabled:opacity-50 border-[#07c6ae] flex items-center space-x-3 space-y-0 peer"]')
    radio_btn2 = ('//*[@class="aspect-square h-4 w-4 rounded-full border-2 justify-center p-2 text-primary shadow '
                  'focus:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed '
                  'disabled:opacity-50 border-[rgba(0,0,0,.54)] flex items-center space-x-3 space-y-0 peer"]')
    radio_btn3 = '//*[@id=":rm:-form-item"]'
    radio_btn4 = '//*[@id=":ro:-form-item"]'
    message = '//*[@id="message"]'


    def larger_files(self, Number,Message):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.larger_files_btn))).click()
        self.loginpage.signin("cediji4499@felibg.com","Tester123@")
        self.driver.find_element(By.XPATH, self.larger_files_btn).click()
        self.driver.find_element(By.XPATH, self.more_btn).click()
        self.driver.find_element(By.CSS_SELECTOR, self.number).send_keys(Number)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.radio_btn4))).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.message).send_keys(Message)
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)
        send_btn = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/slot/slot/slot/div/div/div/form/div/div[6]/button')
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", send_btn)
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)
        send_btn.click()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10)
        time.sleep(5)

    def validLargeFile(self):
        try:
            return self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/slot/slot/slot/div[1]/h2').text
        except NoSuchElementException:
            return False, "Failed to locate message element"

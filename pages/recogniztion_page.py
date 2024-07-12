import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class tashkeel:
    def __init__(self, driver):
        self.driver = driver
    clear_btn='//*[@id="root"]/div[1]/div/div[2]/slot/slot/slot[3]/div/div[1]/button[1]/button'
    texted = '//*[@id="text"]'
    play = '//*[@id="root"]/div[1]/div/div[2]/slot/slot/slot[3]/div/button'

    def recgonation(self, text):
        self.driver.implicitly_wait(5)
        '''enter text '''
        self.driver.find_element(By.XPATH, self.clear_btn).click()
        self.driver.find_element(By.XPATH, self.texted).send_keys(text)
        self.driver.implicitly_wait(5)

        '''play voice'''
        self.driver.find_element(By.XPATH, self.play).click()
        time.sleep(5)
    def validRecgonation(self):
        self.driver.implicitly_wait(5)
        try:
         return self.driver.find_element(By.CSS_SELECTOR,"a[class='sc-bBHGJP kUBPEX']").visible()
        except NoSuchElementException:
            return False


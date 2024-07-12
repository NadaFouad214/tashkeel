import pytest
import softest
from ddt import ddt, file_data
from selenium.webdriver.common.by import By
from pages.login_page import tashkeel
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
@ddt
class TestTashkeel(softest.TestCase):
    """signin"""
    @file_data('C://pycharm_selenium//tashkeel//testdata//tashkeelData.json')
    def test_signInTashkeel(self, email, password):
        si = tashkeel(self.driver)

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[1]/div/header/nav/div[2]/button[2]'))).click()
        si.signin(email, password)
        actual_result = si.validsignIn()
        expectedResult=self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/header/nav/div[2]/div[2]/div/div').is_displayed()
        self.soft_assert(self.assertEqual, expectedResult, actual_result)




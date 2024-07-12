import pytest
import softest
from ddt import ddt, file_data
from selenium.webdriver.common.by import By

from pages.recogniztion_page import tashkeel
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json
import datetime


@pytest.mark.usefixtures("setup")
@ddt
class TestTashkeel(softest.TestCase):
    """signin"""

    @file_data('C:/pycharm_selenium/tashkeel/testdata/tashkeelRecData.json')
    def test_recognationTashkeel(self,text):
        si = tashkeel(self.driver)
        si.recgonation(text)
        actual_result=si.validRecgonation()
        print(actual_result)
        self.assertTrue(actual_result)
        if actual_result:
            print("test pass")
        else:
            print("test faild")
        #self.assert_all()

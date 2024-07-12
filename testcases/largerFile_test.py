import pytest
import softest
from ddt import ddt, file_data
from pages.largerFile_page import tashkeel1



@pytest.mark.usefixtures("setup")
@ddt
class TestTashkeel(softest.TestCase):
    """signin"""


    @file_data('C://pycharm_selenium//tashkeel//testdata//tashkeelLargerFileData.json')
    def test_largerfileTashkeel(self, number,message):
        si = tashkeel1(self.driver)
        si.larger_files(number, message)
        actual_result = si.validLargeFile()
        print(actual_result)
        expectedResult = "تم الارسال"
        self.soft_assert(self.assertEqual, expectedResult, actual_result)
        self.assert_all()
        #print(self.soft_assert(self.assertEqual, expectedResult, actual_result)






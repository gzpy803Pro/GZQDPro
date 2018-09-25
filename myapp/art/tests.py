from django.test import TestCase
from helper import mdjango

# Create your tests here.
class TestLog(TestCase):
    def test_file_log(self):
        mdjango.info('--->test_file_log--')
        a = None
        self.assertIsNone(a, 'a 不是None')
        try:
            a = 1 + '1'
        except:
            mdjango.error('1不能和字符1相加!')


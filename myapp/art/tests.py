from django.test import TestCase
from helper import mdjango

from urllib  import request

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

    def test_qbuy(self):
        # 网络请求测试
        resp = request.urlopen('http://127.0.0.1:8000/book/qbuy/1/')
        print(resp.read().decode())
        self.assertEqual(resp.status, 200)


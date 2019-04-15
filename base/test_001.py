# -*- coding: utf-8 -*-           unittest方法实战

import unittest
from Test import RUNMAIN
import json
import HTMLTestRunner

#创建一个类时必须继承unittest

class  TestMethod(unittest.TestCase):

    def setUp(self):
        #执行前先初始化这个值
        # self.userid=None
        print 'test-------setup'

    def tearDown(self):
        print 'test--------------tearDown'

    def test_001(self):

        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': '888',
            'password': '8888888'
        }

        self.userid = '1002'
        self.running = RUNMAIN(url=url,method='POST',data=data)
        res = self.running.send_main(url=url,method='POST',data=data)

        print res
        print type(res)
        globals()['userid'] = '1002'

        return '------------------------------------'
        print 'test001'

    #跳过对应的case
    # @unittest.skip('test_002')

    def test_002(self):

        print 'test002'


#入口----------********——————————————————**********——————————
if __name__== '__main__':

    #文件路径
    filepath="../report/htmlreport001.html"
    fp=file(filepath,'wb')

    #执行主函数main
    unittest.main()

    #创建一个case容器
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test001'))

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'TTTTTTTTTTTTTTTTTTTT')

    runner.run(suite)
    fp.close()  # 关闭文件流
    #运行整个容器中的case
    # unittest.TextTestRunner().run(suite)


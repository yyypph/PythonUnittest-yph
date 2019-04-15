# -*- coding: utf-8 -*-           unittest方法简单应用

import unittest

#创建一个类时必须继承unittest

class  TestMethod(unittest.TestCase):

    #类方法：只需要执行一次 在这个类之前执行的方法
    @classmethod
    def setUpClass(cls):
        print '这个类执行之前的方法'

    # 类方法：只需要执行一次 在这个类之后执行的方法
    @classmethod
    def tearDownClass(cls):
        print '这个类执行之后的方法'


    def setUp(self):
        print 'test-------setup'

    def tearDown(self):
        print 'test--------------tearDown'

    def test_001(self):
        print 'test001'

    def test_002(self):
        print 'test002'


#入口----------********——————————————————**********——————————
if __name__== '__main__':
    #执行主函数main
    unittest.main()

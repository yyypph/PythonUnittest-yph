# -*- coding: utf-8 -*-           unittest方法实战

import unittest
import json
#导入写好的方法类
from Test import *

#创建一个类时必须继承unittest

class  TestMethod(unittest.TestCase):

    def setUp(self):
        # 实例化---之后就可以用run.来调用这个类中的方法
        self.run = RUNMAIN()

    def test_001(self):

        url = 'http://127.0.0.1:8000/loginget/'
        data = {
            'username': '999',
            'mobile': '999',
            'data': '20179999'
        }

        res = self.run.send_main(url,'GET',data)
        return json.loads(res)
        return '------------------------------------'
    def test_002(self):

        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': '888',
            'password': '8888888'
        }

        res = self.run.send_main(url,'POST',data)
        return json.loads(res)
        return '***************************************'



        print 'test002'


#入口----------********——————————————————**********——————————
if __name__== '__main__':
    #执行主函数main
    unittest.main()

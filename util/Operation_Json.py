# -*- coding: utf-8 -*-         操作json数据       对象：dataconfig

import json

class Operation_Json:

    #构造函数实例化
    def __init__(self):
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        #用完会自动关闭
        with open("../dataconfig/data.json") as fp:
            data = json.load(fp)
            return data

    #根据关键字取数据-返回值
    def get_data(self,key):
        return self.data[key]


#入口----------********——————————————————**********——————————
if __name__== '__main__':
    opjso = Operation_Json()
    print opjso.get_data('login')


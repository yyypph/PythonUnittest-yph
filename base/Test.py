# -*- coding: utf-8 -*-                Get POST方法基础实现逻辑
import requests
import json

#把整个方法都封装成一个雷类
class RUNMAIN:

    #构造函数:实例化类时自动调用一个方法
    #初始化：可以立即调用整个值
    def __init__(self,url,method,data=None):
        #实例化self.res这个值----------可以被后面的函数直接调用
        self.res = self.send_main(url,method,data)

    #POST方法
    def send_post(self,url,data):
        res = requests.post(url=url, data=data).json()
        return  json.dumps(res,indent=2,sort_keys=True)
        return res.json()

    # print send_post(url,data)

    #GET方法
    def send_get(self,url,data):
        res = requests.get(url=url,params=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    # print send_get(urlget,dataget)

    #抽离出一个方法根据传给我的方法类型method
    def send_main(self, url, method, data=None):
        res = None
        if method == 'POST':
            res = self.send_post(url, data)
        else:
            res = self.send_get(url, data)

        return res
        #一定需要打印出来，不然打印台上的数据为none


#入口------------********---------------*******———————————————
if __name__== '__main__':
    # # GET方法的参数
    urlget = 'http://127.0.0.1:8000/loginget/'
    dataget = {
        'username': '1',
        'mobile': '123',
        'data': '20170909'
    }
    # POST方法的参数
    url = 'http://127.0.0.1:8000/login/'
    data = {
        'username': '123',
        'password': '123456'
    }

    #运行整个class类
    run = RUNMAIN(url=url,method='POST',data=data)
    print run.res

    # print run.send_main(url,'POST')
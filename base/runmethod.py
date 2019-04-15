# -*- coding: utf-8 -*-     get post 基类的封装
import sys
sys.path.append("/Volumes/D/pythonCode/")
import requests
import json

class Run_Method:
    #post方法
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
            print res.status_code

        return res.json()

    #get方法
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header,verify=False)
        else:
            res = requests.post(url=url,data=data,verify=False)

        return res.text

    #主方法入口
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)

        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)




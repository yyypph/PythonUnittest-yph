# coding:utf-8


from bmob import *
b =Bmob("b887b832855caff2e0bd03adfb31cc15", "ffd6a28c32f866d9755868b8ecce23f2")



def TestCaseQueryData(self):
    queryresoult = b.find("TestCase",where={"No":0})
    queryresoultjson = queryresoult.jsonData
    print("AAA:",queryresoultjson)

print(TestCaseQueryData(object))


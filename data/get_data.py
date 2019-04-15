# -*- coding: utf-8 -*-         获取测试接口的数据-从Excle中   ---获取接口数据-封装

from util.Operation_Excle import Operation_Excel
import data_config
from  util.Operation_Json import Operation_Json

class GetDada():
    #构造函数-方便下面函数直接调用
    def __init__(self):
        self.opera_Excle = Operation_Excel()

    # 获取Excel中的行数,就是case个数（看成为测试用例数）
    def get_case_lines(self):
        return self.opera_Excle.get_lines()

    #-----------************获取是否执行
    def get_is_run(self,row):
        flag = None
        #传入列的值
        col = int(data_config.get_run())
        #获取该单元格value
        run_model = self.opera_Excle.get_cell_value(row,col)

        #进行判断
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #是否携带header
    def is_header(self,row):
        col = int(data_config.get_header())
        header = self.opera_Excle.get_cell_value(row,col)
        if header == 'yes':
            #若需要header则返回header值
            return data_config.get_header_value()
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col = int(data_config.get_method())
        request_method = self.opera_Excle.get_cell_value(row,col)
        return request_method

    #获取url
    def get_url(self,row):
        col = int(data_config.get_url())
        url = self.opera_Excle.get_cell_value(row,col)
        return url

    #获取请求数据data--------相当于只拿到了key值，具体的value还要到json中去获取根据key
    def get_request_data(self,row):
        col = int(data_config.get_fromdata())
        data = self.opera_Excle.get_cell_value(row,col)

        if data == '':
            return None
        else:
            return data

    #通过获取关键字拿到json数据-----不是所有的data都需要json所以没有进行实例化
    def get_data_for_json(self,row):
        opera_Json = Operation_Json()
        request_data = opera_Json.get_data(self.get_request_data(row))
        return request_data


    #获取预期结果
    def get_expect_data(self,row):
        col = int(data_config.get_expectresoult())
        expect = self.opera_Excle.get_cell_value(row,col)
        if expect == '':
            return None
        return expect

    #获取实际结果
    def write_resoult(self,row,value):
        col = int(data_config.get_actualresoult())
        self.opera_Excle.write_value(row,col,value)


    #----------依赖数据
    #获取依赖数据key
    def get_depend_data(self,row):
        col = int(data_config.get_datadepend())
        depend_key = self.opera_Excle.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key

    #判断是否有case依赖
    def is_depend(self,row):
        col = int(data_config.get_fielddepend())
        depend_case_id = self.opera_Excle.get_cell_value(row,col)

        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_config.get_fielddepend())
        data = self.opera_Excle.get_cell_value(row,col)

        if data == "":
            return None
        else:
            return data
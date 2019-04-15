# -*- coding: utf-8 -*-         设置常量-Excel中的内容-各个参数的行号

class global_var:
#-----------**************************表格中数据Title-------------#
    #测试案例编号
    Case_No = '0'
    Case_Description = '1'
    Request_URL = '2'
    Request_Method = '3'
    Header = '4'
    #依赖数据
    case_depend = '5'
    data_depend = '6'
    field_depend = '7'
    #入参
    From_data = '8'
    #案例是否运行
    is_run = '9'
    Expect_resoult = '10'
    Actual_resoult = '11'
    #测试结果
    Test_resoult = '12'
#-----------**************************表格中数据对应的额方法封装-------------#
#获取case编号
def get_id():
    return global_var.Case_No

def get_description():
    return global_var.Case_Description

#获取url
def get_url():
    return global_var.Request_URL

#获取方式
def get_method():
    return global_var.Request_Method

def get_header():
    return global_var.Header

#--------------Header的值，可以读取配置文件，可以写死，暂时先写死；
def get_header_value():
    header = {
        "header":"1234",
        "cookie":"YPH"
    }

def get_casedepend():
    return global_var.case_depend

def get_datadepend():
    return global_var.data_depend

def get_fielddepend():
    return global_var.field_depend

def get_fromdata():
    return global_var.From_data

#获取是否运行
def get_run():
    return global_var.is_run

def get_expectresoult():
    return global_var.Expect_resoult

def get_actualresoult():
    return global_var.Actual_resoult

def get_testresoult():
    return global_var.Test_resoult
# -*- coding: utf-8 -*-         依赖数据处理(只要被依赖，一定执行，即使 被依赖的case标记为不执行)

from util.Operation_Excle import Operation_Excel
from base.runmethod import Run_Method
from data.get_data import GetDada
from jsonpath_rw import jsonpath,parse
import json

class DependentData:


    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = Operation_Excel()
        self.data = GetDada()

    #通过被依赖的caseid获取该行数据---该行的内容已获取
    def get_case_line_data(self,case_id):
        rows_data = self.opera_excel.get_rows_dada(case_id)
        return rows_data

    #执行获取的内容-获取结果完成
    def run_dependent(self):
        run_method = Run_Method()
        row_mun = self.opera_excel.get_row_num(self.case_id)

        request_data = self.data.get_data_for_json(row_mun)
        header = self.data.is_header(row_mun)
        method = self.data.get_request_method(row_mun)
        url = self.data.get_url(row_mun)
        res = run_method.run_main(method,url,request_data,header)
        return json.loads(res)


    #根据依赖数据的key-去获取依赖case执行response中的对应值 -返回
    def get_data_fro_key(self,row):
        depend_data = self.data.get_depend_data(row)
        response_data = self.run_dependent()

        print depend_data
        print response_data

        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        #循环
        return [math.value for math in madle][0]


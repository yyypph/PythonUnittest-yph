# -*- coding: utf-8 -*-    根据case是否运行-对应的方法的主流程封装
from base.runmethod import Run_Method
from data.get_data import GetDada
from util.common_util import CommonUtil
from data.dependent_data import DependentData

class RunTest:
    def __init__(self):
        self.run_method = Run_Method()
        self.data = GetDada()
        self.com_util = CommonUtil()

    #程序执行
    def go_on_run(self):
        res = None
        #获取行数（case 用例数）
        rows_count = self.data.get_case_lines()
        #开始循环行数执行（第一行标题除去）
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            #已经拿到基础数据---进行判断
            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expect_data(i)
                header = self.data.is_header(i)

                #y依赖条件
                depend_case = self.data.is_depend(i)

                #依赖条件
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    #获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_fro_key(i)

                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    #更新该字段的值
                    request_data[depend_key] = depend_response_data

                res = self.run_method.run_main(method, url, request_data, header)
                print res
                #传入两个值调用Commonutil方法进行比较
                if self.com_util.is_contail(expect,res):
                    print "测试通过"
                    self.data.write_resoult(i,"pass")
                else:
                    print "测试失败"
                    self.data.write_resoult(i,"fail")


            #使用returen只能返回第一个case的response内容-------需用prin
                print res

if __name__== '__main__':
    run = RunTest()
    print run.go_on_run()





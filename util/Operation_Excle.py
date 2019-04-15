# -*- coding: utf-8 -*-         操作Excel表格：获取整个excel中的整体内容       对象：dataconfig
import xlrd
from xlutils.copy import copy


class Operation_Excel:

    #构造函数实例化
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/API.xls'
            self.sheet_id = 0

        self.data = self.get_data()
#----------------------------------------------------------------------------读取数据从excel中
    #获取表sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

#----------------------------------------------------------------------------写入数据往excel中

    def write_value(self,row,col,value):
        #xlrd方法写完之后，前面的单元格内容依然存在
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data) # 不会影响原有的数据
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value) #在内存中操作
        #xlutils最新的2.0版本都只能copy xls格式的excel文件，如果copy的是xlsx再保存，那么新生成的文件将无法打开。
        write_data.save(self.file_name)
        print "---------------------LOG-----写入excel完成"


#------------------------------------------------依赖数据处理
    #根据对应的case_id找到对应的行内容
    def get_rows_dada(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    #根据对应的case_id找到对应行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.data.get_cols_data()
        #循环找到一致的行
        for col_data in clols_data:
            if case_id in col_data:
                return  num
            num = num+1

    #根据对应的行号,找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols

#入口----------********——————————————————**********——————————
if __name__== '__main__':
    opers = Operation_Excel()
    print opers.get_lines()
    print opers.get_cell_value(0,0)


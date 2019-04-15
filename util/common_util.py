# -*- coding: utf-8 -*-       判断预期结果是否包含其中字符串


class CommonUtil:
    def is_contail(self,str_one,str_two):
        '''
        判断一个字符串是否在另一个字符串中
        str_one 查找的字符串
        str_two 备查找的字符串
        '''

        flag = None
        #先进行转码：格式统一后再进行比较
        if isinstance(str_one,unicode):
            str_one = str_one.encode('unicode-escape').decode('string_escape')

        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

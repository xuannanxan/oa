#!/usr/bin/env python
# coding=utf-8
'''
@Description: 
@Author: Xuannan
@Date: 2020-01-29 14:44:44
@LastEditTime : 2020-01-29 15:40:41
@LastEditors  : Xuannan
'''
import xlrd,xlwt
excel = xlrd.open_workbook('./file/demo.xlsx')
table1 = excel.sheet_by_index(0) #根据索引找工作薄
table2 = excel.sheet_by_name('Sheet1') #根据名称找工作薄
# cell,获取单个数据
print(table1.cell_value(2,3))
print(table1.cell(2,3).value)
print(table1.row(2)[3].value)
print(table1.row(2))

new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('1月')
worksheet.write(2,2,'test')
new_workbook.save('./file/test.xls')
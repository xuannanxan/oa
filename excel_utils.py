#!/usr/bin/env python
# coding=utf-8
'''
@Description: 
@Author: Xuannan
@Date: 2020-01-29 15:13:25
@LastEditTime : 2020-01-29 15:51:53
@LastEditors  : Xuannan
'''
import xlrd,xlwt
from xlutils.copy import copy
temp_excel = xlrd.open_workbook('./file/模板.xls',formatting_info=True)
temp_sheet = temp_excel.sheet_by_index(0)
new_excel = copy(temp_excel)
new_sheet = new_excel.get_sheet(0)
# 直接写入
# new_sheet.write(1,1,'13888888888')
# new_sheet.write(2,1,'13888888888')
# new_sheet.write(3,1,'13888888888')
# new_sheet.write(4,1,'13888888888')
# new_sheet.write(5,1,'13888888888')
# new_excel.save('./file/save.xls')

# 带格式写入
# 字体格式
style = xlwt.XFStyle()
font  = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 18*20

style.font = font
# 表格格式
borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN

style.borders = borders
# 对齐
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert =xlwt.Alignment.VERT_CENTER

style.alignment = alignment

new_sheet.write(1,1,'13888888888',style)
new_sheet.write(2,1,'13888888888',style)
new_sheet.write(3,1,'13888888888',style)
new_sheet.write(4,1,'13888888888',style)
new_sheet.write(5,1,'13888888888',style)
new_excel.save('./file/save.xls')

#!/usr/bin/env python
# coding=utf-8
'''
@Description: 
@Author: Xuannan
@Date: 2020-01-29 18:45:04
@LastEditTime : 2020-01-29 19:45:32
@LastEditors  : Xuannan
'''
from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14,17,23,24,27,29,32,31,28,16]
# figure  设置图片样式
plt.figure(figsize=(15,6),dpi=80)

# 绘制X轴的刻度
plt.xticks(range(2,25,2)) # [::2]步长2
# 绘制y轴的刻度
plt.yticks(range(min(y),max(y)+1,2)) # [::2]步长2
# 保存图片
plt.savefig('./01.png')

plt.plot(x,y)
plt.show()
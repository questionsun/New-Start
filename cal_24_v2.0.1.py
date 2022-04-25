#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import I
from tkinter import *
import hashlib
import time
import inspect
from typing import List

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        #主窗口
        self.init_window_name.title("计算24_v2.2")           
        self.init_window_name.geometry('1000x560+150+150')

        #标签
        self.init_data_label = Label(self.init_window_name, text="请选择需要计算的四个数")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出计算结果")
        self.result_data_label.grid(row=8,column=0)

        self.choice_data1_label = Label(self.init_window_name, text="数字选择列表")
        self.choice_data1_label.grid(row=1,column=1)

        #列表窗口
        num = [1,2,3,4,5,6,7,8,9,10]
        self.choice_data_box = Listbox(self.init_window_name)
        for item in num:
            self.choice_data_box.insert("end",item)
        self.choice_data_box.grid(row=2,rowspan=5,column=1)

        list = ['第一个数','第二个数','第三个数','第四个数']
        self.confirm_data_box = Listbox(self.init_window_name)
        for item in list:
            self.confirm_data_box.insert("end",item)
        self.confirm_data_box.grid(row=2,rowspan=5,column=3)

        #结果文本框
        self.result_data_Text = Text(self.init_window_name, width=100, height=10)  #处理结果展示
        self.result_data_Text.grid(row=9, column=1,columnspan=3)

        #按钮
        self.data1_confirm_button = Button(self.init_window_name, text="确定第一个数", bg="lightblue", width=10,command=lambda:self.select(0)) 
        self.data1_confirm_button.grid(row=2, column=2)        
        self.data2_confirm_button = Button(self.init_window_name, text="确定第二个数", bg="lightblue", width=10,command=lambda:self.select(1)) 
        self.data2_confirm_button.grid(row=3, column=2)
        self.data3_confirm_button = Button(self.init_window_name, text="确定第三个数", bg="lightblue", width=10,command=lambda:self.select(2)) 
        self.data3_confirm_button.grid(row=4, column=2)        
        self.data4_confirm_button = Button(self.init_window_name, text="确定第四个数", bg="lightblue", width=10,command=lambda:self.select(3)) 
        self.data4_confirm_button.grid(row=5, column=2)
        self.cal_start_button = Button(self.init_window_name, text="开始计算", bg="lightblue", width=10,command=self.cal_24)  # 调用内部方法  加()为直接调用
        self.cal_start_button.grid(row=11, column=1)
        self.cal_close_button = Button(self.init_window_name, text="退出", bg="lightblue", width=10,command=self.init_window_name.destroy)  # 调用内部方法  加()为直接调用
        self.cal_close_button.grid(row=11, column=3)

    #在数字框内确认数字
    def select(self,select_button):
        str_temp = self.choice_data_box.curselection()[0]
        var = int(str_temp)+1
        ll = "第" + str(select_button+1) + "个数为:" + str(var)
        self.confirm_data_box.insert((select_button+1),ll)
        self.confirm_data_box.delete(select_button)

    #计算24并输出结果
    def cal_24(self):
        num = []
        for i in range(4):
            num.append(int(str(self.confirm_data_box.get(i,i)[0])[6:]))
        result_list = cal_24_in(num)
        self.result_data_Text.delete(1.0,END)
        if len(result_list) == 0:
            self.result_data_Text.insert(1.0,"没有结果")
        else:
            for result in result_list:
                self.result_data_Text.insert(1.0,("".join(map(str,result[1:12]))+'=24'+'\n'))

#用分数计算重新定义加减乘除
def cal(num1,num2,cal_sign):
    if cal_sign == "+":
        return [num1[0]*num2[1]+num1[1]*num2[0],num1[1]*num2[1]]
    if cal_sign == '-':
        return [num1[0]*num2[1]-num1[1]*num2[0],num1[1]*num2[1]]
    if cal_sign == '*':
        return [num1[0]*num2[0],num1[1]*num2[1]]
    if cal_sign == '/':
        return [num1[0]*num2[1],num1[1]*num2[0]]

#第一种情形，((a+b)+c)+d
def type_1(num,sign):
    status = False
    cal_result = cal(cal(cal(num[0],num[1],sign[0]),num[2],sign[1]),num[3],sign[2])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print('(('+repr(num1[0])+sign[0]+repr(num2[0])+')'+sign[1]+repr(num3[0])+')'+sign[2]+repr(num4[0]))
        status = True
    ret_result = [status,'(','(',num[0][0],sign[0],num[1][0],')',sign[1],num[2][0],')',sign[2],num[3][0]]
    return ret_result

#第二种情形,(a+b)+(c+d)
def type_2(num,sign):    
    status = False
    cal_result = cal(cal(num[0],num[1],sign[0]),cal(num[2],num[3],sign[2]),sign[1])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print('('+repr(num1[0])+sign[0]+repr(num2[0])+')'+sign[1]+'('+repr(num3[0])+sign[2]+repr(num4[0])+')')
        status = True
    ret_result = [status,'(',num[0][0],sign[0],num[1][0],')',sign[1],'(',num[2][0],sign[2],num[3][0],')']
    return ret_result

#第三种情形,(a+(b+c))+d
def type_3(num,sign):    
    status = False
    cal_result = cal(cal(num[0],cal(num[1],num[2],sign[1]),sign[0]),num[3],sign[2])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print('('+repr(num1[0])+sign[0]+'('+repr(num2[0])+sign[1]+repr(num3[0])+'))'+sign[2]+repr(num4[0]))
        status = True
    ret_result = [status,'(',num[0][0],sign[0],'(',num[1][0],sign[1],num[2][0],')',')',sign[2],num[3][0]]
    return ret_result        

#第四种情形,a+((b+c)+d)
def type_4(num,sign):    
    status = False
    cal_result = cal(num[0],cal(cal(num[1],num[2],sign[1]),num[3],sign[2]),sign[0])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print(repr(num1[0])+sign[0]+'(('+repr(num2[0])+sign[1]+repr(num3[0])+')'+sign[2]+repr(num4[0])+')')
        status = True
    ret_result = [status,num[0][0],sign[0],'(','(',num[1][0],sign[1],num[2][0],')',sign[2],num[3][0],')']
    return ret_result   
                
#第五种情形,a+(b+(c+d))
def type_5(num,sign):
    status = False
    cal_result = cal(num[0],cal(num[1],cal(num[2],num[3],sign[2]),sign[1]),sign[0])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print(repr(num1[0])+sign[0]+'('+repr(num2[0])+sign[1]+'('+repr(num3[0])+sign[2]+repr(num4[0])+'))')
        status = True
    ret_result = [status,num[0][0],sign[0],'(',num[1][0],sign[1],'(',num[2][0],sign[2],num[3][0],')',')']
    return ret_result

#所有可能的符号位置
def all_sign():               
    sign = ['+','-','*','/']
    sign_all = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                    sign_all.append([sign[i],sign[j],sign[k]])
    return sign_all

#所有可能的数字位置
def all_num(num):    
    number_all = []
    for i in range(4):
        num_tmp1 = num.copy()
        num1 = num_tmp1[i]
        del num_tmp1[i]
        for j in range(3):
            num_tmp2 = num_tmp1.copy() 
            num2 = num_tmp2[j]
            del num_tmp2[j]
            for k in range(2):
                num_tmp3 = num_tmp2.copy()
                num3 = num_tmp3[k]
                del num_tmp3[k]
                for l in range(1):
                    num_tmp4 = num_tmp3
                    num4 = num_tmp4[l]
                    if [num1,num2,num3,num4] not in number_all:
                        number_all.append([num1,num2,num3,num4])
    return number_all    

#内部计算过程，返回成功的列表
def cal_24_in(var):
    result_list = []
    num_all = all_num(var)
    sign_all = all_sign()
    for number_on in num_all:
        var_on = [[number_on[0],1],[number_on[1],1],[number_on[2],1],[number_on[3],1]]
        for sign_on in sign_all:
            for i in range(1,6):
                result = eval("type_" + str(i))(var_on,sign_on)
                if result[0] == True and (result not in result_list):
                    result_list.append(result)
    return result_list
   
def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
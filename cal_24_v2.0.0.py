#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import I
from tkinter import *
import hashlib
import time
import inspect
from typing import List

LOG_LINE_NUM = 0
global var1
global var2
sign = ['+','-','*','/']
success = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        #主窗口
        self.init_window_name.title("计算24_v2.2")           
        self.init_window_name.geometry('1000x800+10+10')

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
        self.result_data_Text.grid(row=9, column=1,columnspan=7)

        #按钮
        self.data1_confirm_button = Button(self.init_window_name, text="确定第一个数", bg="lightblue", width=10,command=self.select1) 
        self.data1_confirm_button.grid(row=2, column=2)        
        self.data2_confirm_button = Button(self.init_window_name, text="确定第二个数", bg="lightblue", width=10,command=self.select2) 
        self.data2_confirm_button.grid(row=3, column=2)
        self.data3_confirm_button = Button(self.init_window_name, text="确定第三个数", bg="lightblue", width=10,command=self.select3) 
        self.data3_confirm_button.grid(row=4, column=2)        
        self.data4_confirm_button = Button(self.init_window_name, text="确定第四个数", bg="lightblue", width=10,command=self.select4) 
        self.data4_confirm_button.grid(row=5, column=2)
        self.cal_start_button = Button(self.init_window_name, text="开始计算", bg="lightblue", width=10,command=self.cal_24)  # 调用内部方法  加()为直接调用
        self.cal_start_button.grid(row=11, column=1)
        self.cal_close_button = Button(self.init_window_name, text="退出", bg="lightblue", width=10,command=self.init_window_name.destroy)  # 调用内部方法  加()为直接调用
        self.cal_close_button.grid(row=11, column=7)  

    def select1(self):
        var1 = int(self.choice_data_box.curselection()[0])+1
        l1 = "第一个数为:" + str(var1)
        self.confirm_data_box.insert(1,l1)
        self.confirm_data_box.delete(0)

    def select2(self):
        var2 = int(self.choice_data_box.curselection()[0])+1
        l2 = "第二个数为:" + str(var2)
        self.confirm_data_box.insert(2,l2)
        self.confirm_data_box.delete(1)

    def select3(self):
        var3 = int(self.choice_data_box.curselection()[0])+1
        l3 = "第三个数为:" + str(var3)
        self.confirm_data_box.insert(3,l3)
        self.confirm_data_box.delete(2)

    def select4(self):
        var4 = int(self.choice_data_box.curselection()[0])+1
        l4 = "第四个数为:" + str(var4)
        self.confirm_data_box.insert(4,l4)
        self.confirm_data_box.delete(3)

    def cal_24(self):
        num0 = int(str(self.confirm_data_box.get(0,0)[0])[6:])
        num1 = int(str(self.confirm_data_box.get(1,1)[0])[6:])
        num2 = int(str(self.confirm_data_box.get(2,2)[0])[6:])
        num3 = int(str(self.confirm_data_box.get(3,3)[0])[6:])
        result_list = cal_24_in(num0,num1,num2,num3)
        self.result_data_Text.delete(1.0,END)
        if len(result_list) == 0:
            self.result_data_Text.insert(1.0,"没有结果")
        else:
            for result in result_list:
                self.result_data_Text.insert(1.0,("".join(map(str,result[1:12]))+'=24'+'\n'))

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
def type_1(num1,num2,num3,num4,sign):
    status = False
    cal_result = cal(cal(cal(num1,num2,sign[0]),num3,sign[1]),num4,sign[2])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print('(('+repr(num1[0])+sign[0]+repr(num2[0])+')'+sign[1]+repr(num3[0])+')'+sign[2]+repr(num4[0]))
        status = True
    ret_result = [status,'(','(',num1[0],sign[0],num2[0],')',sign[1],num3[0],')',sign[2],num4[0]]
    return ret_result

#第二种情形,(a+b)+(c+d)
def type_2(num1,num2,num3,num4,sign):    
    status = False
    cal_result = cal(cal(num1,num2,sign[0]),cal(num3,num4,sign[2]),sign[1])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print('('+repr(num1[0])+sign[0]+repr(num2[0])+')'+sign[1]+'('+repr(num3[0])+sign[2]+repr(num4[0])+')')
        status = True
    ret_result = [status,'(',num1[0],sign[0],num2[0],')',sign[1],'(',num3[0],sign[2],num4[0],')']
    return ret_result

#第三种情形,(a+(b+c))+d
def type_3(num1,num2,num3,num4,sign):    
    status = False
    cal_result = cal(cal(num1,cal(num2,num3,sign[1]),sign[0]),num4,sign[2])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print('('+repr(num1[0])+sign[0]+'('+repr(num2[0])+sign[1]+repr(num3[0])+'))'+sign[2]+repr(num4[0]))
        status = True
    ret_result = [status,'(',num1[0],sign[0],'(',num2[0],sign[1],num3[0],')',')',sign[2],num4[0]]
    return ret_result        

#第四种情形,a+((b+c)+d)
def type_4(num1,num2,num3,num4,sign):    
    status = False
    cal_result = cal(num1,cal(cal(num2,num3,sign[1]),num4,sign[2]),sign[0])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print(repr(num1[0])+sign[0]+'(('+repr(num2[0])+sign[1]+repr(num3[0])+')'+sign[2]+repr(num4[0])+')')
        status = True
    ret_result = [num1[0],sign[0],'(','(',num2[0],sign[1],num3[0],')',sign[2],num4[0],')']
    return ret_result   
                
#第五种情形,a+(b+(c+d))
def type_5(num1,num2,num3,num4,sign):    
    status = False
    cal_result = cal(num1,cal(num2,cal(num3,num4,sign[2]),sign[1]),sign[0])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
#        print(repr(num1[0])+sign[0]+'('+repr(num2[0])+sign[1]+'('+repr(num3[0])+sign[2]+repr(num4[0])+'))')
        status = True
    ret_result = [num1[0],sign[0],'(',num2[0],sign[1],'(',num3[0],sign[2],num4[0],')',')']
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
def all_num(var1,var2,var3,var4):    
    num = [var1,var2,var3,var4]
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
                    number_all.append([num1,num2,num3,num4])
    return number_all    


#内部计算过程，返回可能的列表
def cal_24_in(var1,var2,var3,var4):
    result_list = []
    all_number = all_num(var1,var2,var3,var4)
    sign_all = all_sign()
    for number_on in all_number:
        num1 = [number_on[0],1]
        num2 = [number_on[1],1]
        num3 = [number_on[2],1]
        num4 = [number_on[3],1]
        for sign_on in sign_all:
            result = type_1(num1,num2,num3,num4,sign_on)
            if result[0] == True and (result not in result_list):
                result_list.append(result)
            result = type_2(num1,num2,num3,num4,sign_on)
            if result[0] == True and (result not in result_list):
                result_list.append(result)            
            result = type_3(num1,num2,num3,num4,sign_on)
            if result[0] == True and (result not in result_list):
                result_list.append(result)
            result = type_4(num1,num2,num3,num4,sign_on)
            if result[0] == True and (result not in result_list):
                result_list.append(result)
            result = type_5(num1,num2,num3,num4,sign_on) 
            if result[0] == True and (result not in result_list):
                result_list.append(result)
    for result in result_list:
        print(" ".join(map(str,result[1:12])))
    return result_list



   
def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
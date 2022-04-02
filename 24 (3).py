#!/usr/bin/env python
# coding: utf-8

# In[304]:


#算24中使用的加减乘除
def cal_add(num1,num2):    #第一个数加第二个数
    return [num1[0]*num2[1]+num1[1]*num2[0],num1[1]*num2[1]]

def cal_sub(num1,num2):    #第一个数减第二个数
    return [num1[0]*num2[1]-num1[1]*num2[0],num1[1]*num2[1]]

def cal_mul(num1,num2):    #第一个数乘第二个数
    return [num1[0]*num2[0],num1[1]*num2[1]]

def cal_div(num1,num2):    #第一个数减第二个数
    return [num1[0]*num2[1],num1[1]*num2[0]]

def cal(num1,num2,cal_sign):    #根据不同符号选择加减乘除进行计算
    if cal_sign == "+":
        return cal_add(num1,num2)
    if cal_sign == '-':
        return cal_sub(num1,num2)
    if cal_sign == '*':
        return cal_mul(num1,num2)
    if cal_sign == '/':
        return cal_div(num1,num2)


# In[370]:


#提供四个数字的不同排列方法,返回一个列表，每四个为一个元素
def cal_number(num1,num2,num3,num4):
    num = [[num1,1],[num2,1],[num3,1],[num4,1]]
    all_n = [num]
    for i in range(len(num)):
        t1 = num.copy()
        n1 = t1.pop(i)
        for j in range(len(t1)):
            t2 = t1.copy()
            n2 = t2.pop(j)
            for k in range(len(t2)):
                t3 = t2.copy()
                n3 = t3.pop(k)
                n4 = t3[0]
                all_n.append([n1,n2,n3,n4])
    del all_n[0]
    return all_n


# In[364]:


#提供四种符号中的三种,返回一个列表，每三个为一个元素
def cal_sign(sign):
    all_sign = [[sign[0],sign[0],sign[0]]]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                all_sign.append([sign[i],sign[j],sign[k]])
    del all_sign[0]
    return all_sign


# In[374]:


def cal_24(num1,num2,num3,num4,sign):
    all_num = cal_number(num1,num2,num3,num4)
    all_sign = cal_sign(sign)
    S_1 = False
    S_2 = False
    S_3 = False
    S_4 = False
    S_5 = False
    for i in range(len(all_num)):
        for j in range(len(all_sign)):
            print(all_num[i],all_sign[j])
            S_1 = S_1 or first(all_num[i],all_sign[j])
            S_2 = S_2 or second(all_num[i],all_sign[j])
            S_3 = S_3 or third(all_num[i],all_sign[j])
            S_4 = S_4 or forth(all_num[i],all_sign[j])
            S_5 = S_5 or fifth(all_num[i],all_sign[j])                    
    if S_1 or S_2 or S_3 or S_4 or S_5 == True:
        return True
    else:
        return False
                         
def first(num,sign_1):    #第一种情形
    status = False
    cal_result = cal(cal(cal(num[0],num[1],sign_1[0]),num[2],sign_1[1]),num[3],sign_1[2])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print('(('+repr(num[0][0])+sign_1[0]+repr(num[1][0])+')'+sign_1[1]+repr(num[2][0])+')'+sign_1[2]+repr(num[3][0]))
        status = True
    return status

def second(num,sign_2):    #第二种情形
    status = False
    cal_result = cal(cal(num[0],num[1],sign_2[0]),cal(num[2],num[3],sign_2[2]),sign_2[1])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print('('+repr(num[0][0])+sign_2[0]+repr(num[1][0])+')'+sign_2[1]+'('+repr(num[2][0])+sign_2[2]+repr(num[3][0])+')')
        status = True
    return status

def third(num,sign_3):    #第三种情形
    status = False
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]
    num4 = num[3]
    cal_result = cal(cal(num1,cal(num2,num3,sign_3[1]),sign_3[0]),num4,sign_3[2])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print('('+repr(num1[0])+sign_3[0]+'('+repr(num2[0])+sign_3[1]+repr(num3[0])+'))'+sign_3[2]+repr(num4[0]))
        status = True
    return status        

def forth(num,sign_4):    #第四种情形
    status = False
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]
    num4 = num[3]
    cal_result = cal(num1,cal(cal(num2,num3,sign_4[1]),num4,sign_4[2]),sign_4[0])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print(repr(num1[0])+sign_4[0]+'(('+repr(num2[0])+sign_4[1]+repr(num3[0])+')'+sign_4[2]+repr(num4[0])+')')
        status = True
    return status   
                
def fifth(num,sign_5):    #第五种情形
    status = False
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]
    num4 = num[3]
    cal_result = cal(num1,cal(num2,cal(num3,num4,sign_5[2]),sign_5[1]),sign_5[0])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print(repr(num1[0])+sign_5[0]+'('+repr(num2[0])+sign_5[1]+'('+repr(num3[0])+sign_5[2]+repr(num4[0])+'))')
        status = True
    return status


# In[376]:


#主程序

sign = ['+','-','*','/']
success = 0

num1 = 4
num2 = 4
num3 = 4
num4 = 4
cal_24(num1,num2,num3,num4,sign)

print(success)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[280]:


def cal_add(num1,num2):    #第一个数加第二个数
    num3 = [num1[0]*num2[1]+num1[1]*num2[0],num1[1]*num2[1]]
    return num3

def cal_sub(num1,num2):    #第一个数减第二个数
    num3 = [num1[0]*num2[1]-num1[1]*num2[0],num1[1]*num2[1]]
    return num3

def cal_mul(num1,num2):    #第一个数乘第二个数
    num3 = [num1[0]*num2[0],num1[1]*num2[1]]
    return num3

def cal_div(num1,num2):    #第一个数减第二个数
    num3 = [num1[0]*num2[1],num1[1]*num2[0]]
    return num3

def cal(num1,num2,sign_on):    #根据不同符号选择加减乘除进行计算
    var1 = num1
    var2 = num2
    cal_sign = sign_on
    if cal_sign == "+":
        return cal_add(var1,var2)
    if cal_sign == '-':
        return cal_sub(var1,var2)
    if cal_sign == '*':
        return cal_mul(var1,var2)
    if cal_sign == '/':
        return cal_div(var1,var2)

def cal_24(num1,num2,num3,num4,sign,count):
    S_1 = False
    S_2 = False
    S_3 = False
    S_4 = False
    S_5 = False
    for i in range(4):
        for j in range(4):
             for k in range(4):
                    sign_on = [sign[i],sign[j],sign[k]]
                    S_1 = S_1 or first(num1,num2,num3,num4,sign_on)
                    S_2 = S_2 or second(num1,num2,num3,num4,sign_on)
                    S_3 = S_3 or third(num1,num2,num3,num4,sign_on)
                    S_4 = S_4 or forth(num1,num2,num3,num4,sign_on)
                    S_5 = S_5 or fifth(num1,num2,num3,num4,sign_on)                    
    if S_1 or S_2 or S_3 or S_4 or S_5 == True:
        count = count + 1
    return count
                         
def first(num1,num2,num3,num4,sign_1):    #第一种情形
    status = False
    cal_result = cal(cal(cal(num1,num2,sign_1[0]),num3,sign_1[1]),num4,sign_1[2])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print('(('+repr(num1[0])+sign_1[0]+repr(num2[0])+')'+sign_1[1]+repr(num3[0])+')'+sign_1[2]+repr(num4[0]))
        status = True
    return status

def second(num1,num2,num3,num4,sign_2):    #第二种情形
    status = False
    cal_result = cal(cal(num1,num2,sign_2[0]),cal(num3,num4,sign_2[2]),sign_2[1])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print('('+repr(num1[0])+sign_2[0]+repr(num2[0])+')'+sign_2[1]+'('+repr(num3[0])+sign_2[2]+repr(num4[0])+')')
        status = True
    return status

def third(num1,num2,num3,num4,sign_3):    #第三种情形
    status = False
    cal_result = cal(cal(num1,cal(num2,num3,sign_3[1]),sign_3[0]),num4,sign_3[2])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print('('+repr(num1[0])+sign_3[0]+'('+repr(num2[0])+sign_3[1]+repr(num3[0])+'))'+sign_3[2]+repr(num4[0]))
        status = True
    return status        

def forth(num1,num2,num3,num4,sign_4):    #第四种情形
    status = False
    cal_result = cal(num1,cal(cal(num2,num3,sign_4[1]),num4,sign_4[2]),sign_4[0])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print(repr(num1[0])+sign_4[0]+'(('+repr(num2[0])+sign_4[1]+repr(num3[0])+')'+sign_4[2]+repr(num4[0])+')')
        status = True
    return status   
                
def fifth(num1,num2,num3,num4,sign_5):    #第五种情形
    status = False
    cal_result = cal(num1,cal(num2,cal(num3,num4,sign_5[2]),sign_5[1]),sign_5[0])
    if cal_result[1] != 0 and cal_result[0]/cal_result[1] == 24:
        print(repr(num1[0])+sign_5[0]+'('+repr(num2[0])+sign_5[1]+'('+repr(num3[0])+sign_5[2]+repr(num4[0])+'))')
        status = True
    return status
        
def start_24(var1,var2,var3,var4,sign):    #调整四个数字的位置
    num = [var1,var2,var3,var4]
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
                    cal_24(num1,num2,num3,num4,sign)
        
    
#程序开始
sign = ['+','-','*','/']
success = 0
for i in range(10):
    num1 = [i+1,1]
    for j in range(10):
        num2 = [j+1,1]
        for k in range(10):
            num3 = [k+1,1]
            for l in range(10):
                num4 = [l+1,1]
                print(num1[0],num2[0],num3[0],num4[0])
                success = cal_24(num1,num2,num3,num4,sign,success)
print(success)


# In[ ]:





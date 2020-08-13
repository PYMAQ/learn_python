# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

#1.投机取巧解法
def plusOne(digits):
    if(digits[0]==0):
        return [1]
    else:
        new_digit=[]
        def cheng(x,y):
            return x*10+y
        from functools import  reduce
        value=reduce(cheng,digits)
        value+=1
        for i in str(value):
            new_digit.append(int(i))
    return new_digit

digits=[9,9,9,9,9,9]
#digits=[1,2,3]
print(plusOne(digits))

#2.逆序遍历原数组
def re_travel(digits):
    for i in range(len(digits)-1,-1,-1):
        if(digits[i]==9):
            digits[i]=0
        else:
            digits[i]+=1
            return digits

    if(digits[0]==0):
        digits.append(0)
        digits[0]=1
    return  digits

digits = [9, 9, 9, 9, 9, 9]
# digits=[1,2,3]
print(re_travel(digits))
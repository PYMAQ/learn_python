#1.变量可以指向函数
print(abs(-10))

#注意不要加括号，传递的是函数的名称
f=abs

print(f(-10))
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

#2、map特性
def f(x):
    return x*x

list=map(f,[1,2,3,4,5,54,6,7,8,9,10])
for i in  list:
    print(str(i)+' ',end='')

print()


#3.reduce特性
def f1(x,y):
    return x*10+y
from functools import reduce
print(reduce(f1,[1,2,3,4,5,6,7,8,9,10]))


#4.练习1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
list2=['adam', 'LISA', 'barT']

def char2upper(name):
    return name[0].upper() + name[1:].lower()
    #return str.capitalize(name) 直接将字符串第一个字符变成大写，其余变成小写

map_2upper=map(char2upper,list2)

for i in map_2upper:
    print(i)


#5.练习2
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def prod(L):
    return reduce(get_product,L)

def get_product(x,y):
    return x*y

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


#6.练习3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    #获取字符串的总长度
    a = len(s)
    #获取字符串中.的下标
    b = s.index(".")
    #定义数字字典
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    #定义函数，根据字符返回数字
    def fn(s):
        return DIGITS[s]
    #先用map把整数部分的数字进行返回并利用lambda累乘加得到一个整数部分的数字
    s1 = reduce(lambda x, y: x * 10 + y, map(fn, s[:b]))
    # print(s1)
    #再用map把小数部分的数字进行返回并利用lambda累乘加得到小数部分的数字
    s2 = reduce(lambda x, y: x * 10 + y, map(fn, s[b + 1:]))
    # print(s2)
    return s1 + s2 * (10 ** (b - a + 1))

print('str2float(\'123.456\') =', str2float('1213.456'))
if abs(str2float('1213.456') - 1213.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

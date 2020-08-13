
d = {'a': 1, 'b': 2, 'c': 3}
#1.迭代字典的key和value，同时按顺序迭代
for k,v in d.items():
    print(k)
    print(v)
print('--------------------')

#2.迭代字典的key或者value
for k in d.keys():
    print(k)

for v in d.values():
    print(v)
print('--------------------')

#3.迭代字符串
str='xxyyzzPythonNB'
for s in  str:
    print(s+'  ',end='')

print('\n--------------------')
#4.判断是否可以迭代
from collections import Iterable
print(isinstance(123, Iterable))
print(isinstance(str, Iterable))
print(isinstance(d, Iterable))

print('--------------------')

#5.enumerate,根据下标筛选list数组的值
list=['jqz','wsy','jkqswjx','iuia']
for i,value in enumerate(list):
    if(i>=2):
        print(i,end='')
        print(value)

#6.请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findmaxmin(L):
    max = L[0]
    min = L[0]
    for i, v in enumerate(L):
        if (v > max): max = L[i]
        if (v < min): min = L[i]

    return (min, max)

findmaxmin([7, 1, 3, 9, 5])
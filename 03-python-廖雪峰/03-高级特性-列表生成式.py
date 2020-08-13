#简介：可以自动生成list的内置语法

#1.要生成一个【平方数】列表
list=[x * x  for x in range(1,20)]
print(list)

#2.要生成一个【仅是偶数的平方数的】列表
list2=[x*x for x in range(1,20) if (x*x)%2==0 ]
print(list2)

#3.列出当前目录下的所有文件名和目录名
import  os
dir_list=[d for d in  os.listdir('.')]
print(dir_list)

#4.列表生成式，同时遍历字典中的k和v
dict={'海贼王':'2','wsy':'12','211':'985'}
list3=[k+'='+v for k,v in dict.items()]
list3_1=[v for v in dict.values()]
print(list3)
print(list3_1)


#5.两层循环全排列
list4=[m+n for m in 'xyz' for n in 'abc']
print(list4)

#6.练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower()  for x in L1 if isinstance(x,str)]
L3 = [s.lower() if isinstance(s , str) else s for s in L1]
print(L2)
print(L3)
#总结：列表生成式中，if可以很灵活的放在前面或者后面，如果放在前面则必须有else，如果放在for后面则不能有else
#疑问，怎么使用python列表生成式实现前置if-else？？？

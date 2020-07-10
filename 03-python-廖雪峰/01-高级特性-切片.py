data = ["A", "B", "C", "D", "E", 'F', 'G', 'H', 'I', 'J', 'K']
# 正着数  0   1     2    3    4    5    6    7    8    9   10     共11个元素
# 倒着数  10  9     8    7    6    5    4       0     共11个元素

print(len(data))
#1.取data列表前面下标为0到3的元素
print(data[:4])#等价于data[0:4]
print('--------上面是第1点------------')
#2.取出倒数第6个元素 记住倒数第一个元素的索引是-1。
print(data[-6])
print('--------上面是第2点------------')

#3.取出倒数的5个元素
print(data[-5:])
print('--------上面是第3点------------')

#4.前8个数每间隔2个数取出一个
print(data[:8:2])
print('--------上面是第4点------------')

#所有数字 每3个取1个
print(data[::2])
print('--------上面是第4点------------')

# 5.利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
juzi='       hELLO     '
juzi_new=' '
for i in range(len(juzi)):
    if juzi[i]!=' ':
        print(juzi[i])
        juzi_new.join(str(juzi[i]))
juzi=juzi_new
print(juzi_new)

print('--------上面是第5点------------')

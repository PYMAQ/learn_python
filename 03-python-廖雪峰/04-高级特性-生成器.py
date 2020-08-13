
#1.生成器
#遍历三次方，并逐个输出，生成算法,已经遍历到的，后面不会遍历
list1=(i*i*i for i in range(1,11))
print(list1)
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
for i in list1:
    print(i)

#2.普通函数和generator函数
# 普通函数调用直接返回结果

# generator函数的“调用”实际返回一个generator对象：


#3.生成杨辉三角
def triangles():
    t = [1]
    yield t
    t = [1, 1]
    yield t
    while True:
        t1 = [0 for i in range(0, len(t) + 1)]
        t1[0] = 1
        t1[-1] = 1
        i = 0
        j = 1
        k = 1
        while j <= len(t) - 1:
            v = t[i] + t[j]
            t1[k] = v
            i = i + 1
            j = j + 1
            k = k + 1
        t = t1
        yield t
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break
for t in results:
    print(t)

#列表前面加星号作用是将列表解开成两个独立的参数，传入函数，
# 字典前面加两个星号，是将字典解开成独立的元素作为形参。
#通俗的说：zip()压缩可迭代对象，*号解压可迭代对象；

#优秀的解法
def get_triuangles(n):
    previous = [1]
    while n:
        yield previous
        previous = [1]+ [previous[i] + previous[i + 1] for i in range(len(previous) - 1)]+ [1]
        #第二种形式 previous=[1,*[previous[i]+previous[i+1] for i in range(len(previous)-1),1]
        n-=1

for i in  get_triuangles(20):
    print(i)
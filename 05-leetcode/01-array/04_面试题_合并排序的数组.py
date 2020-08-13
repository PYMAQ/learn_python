from typing import List


#解法一:倒序填充法
def merge_reverse(A, m, B, n):
    A.reverse()
    B.reverse()
    for i in  range(len(B)):
        A[i]=B[i]
    A.reverse()
    A.sort()
    return A

# 解法一:切片法
def merge_slice(A, m, B, n):
        A[m: ] = B
        A.sort()
        return A



#解法二：双指针队列法
def merge_double_queue(A, m, B, n):

    return A



A = [1,2,3,0,0,0]
m = 3
B = [2,5,6]
n = 3
print(merge_reverse(A,m,B,n))

A = [1,2,3,0,0,0]
m = 3
B = [2,5,6]
n = 3
print(merge_slice(A,m,B,n))

A = [1,2,3,0,0,0]
m = 3
B = [2,5,6]
n = 3
print(merge_double_queue(A,m,B,n))
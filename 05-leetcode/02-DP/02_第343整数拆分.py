#给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。


#解法1：暴力
def integerBreak(n):
    len=len(n)
    list_num=[ i+1 for i in range(len-1)]
    for i in range(0,len):
        pass
n=10
print(integerBreak(n))
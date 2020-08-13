
#解法一：动态规划
def solve(idx,nums):
    if(idx<0):
        return 0
    else:
        return max(nums[idx]+solve(idx-2,nums),solve(idx-1,nums))

def rob(nums):
    return solve(len(nums)-1,nums)

nums=[1,2,3]
print(rob(nums))

#解法一.动态规划一个函数版本
def solve(idx,nums):
    if(idx<0):
        return 0
    else:
        return max(nums[idx]+solve(idx-2,nums),solve(idx-1,nums))

def rob(nums):
    return solve(len(nums)-1,nums)

nums=[1,2,3]
print(rob(nums))
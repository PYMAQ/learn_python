from typing import List


#解法一:快慢双指针法
def removeDuplicates_double_pointer(nums):
    #for i in range(len(nums)):
    #第一个指针初始化
    i = 0
    #第二个指针初始化
    j = 1
    #两个指针对应的字符不同则交换，c指交换的次数
    c = 0

    #j和i要在nums的长度范围内
    while (j + 1 <= len(nums) and (i + 1 <= len(nums))):
        #如果两个指针对应的值相等，则第二个指针后移一位
        if (nums[i] == nums[j]):
            j += 1
        #如果两个指针对应的值不等，则进入else
        else:
            #i后移一位，第一指针执行的值为交换值
            i += 1
            #交换第一指针和第二指针的值
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            #第二指针后移一位，
            j += 1
            #交换次数加一，
            c += 1
    #返回原来数组的0到交换次数的list（部分list）
    return len(nums[0:c + 1])

#解法二：原地删除法_python或者有pop方法的才有
def removeDuplicates(nums):
    i = 0
    while (len(nums)-i-1 > 0):
         if nums[i+1] == nums[i]:
            nums.pop(i)
         else:
            i += 1
    return len(nums)

#解法二：反向遍历解法或者叫从后往前删除法
def remove_re(nums):
    #range(开始的位置，结束的位置，步长)
    for num_index in range(len(nums) - 1, 0, -1):
        #从nums的最后一个开始遍历, 然后与前一个进行对比，如果相等则删除该位置的数，不等则继续往前遍历
        if nums[num_index] == nums[num_index - 1]:
            nums.pop(num_index)
    print(nums)
    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates_double_pointer(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_re(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
for i in range(len(nums)-1,-1,-1):
    print(nums[i])




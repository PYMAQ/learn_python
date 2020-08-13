# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

#解法1：贪心算法
def maxSubArray(nums):
    # 时间复杂度：O(n),遍历了一遍
    # 空间复杂度:O(1)，用了2个变量
    cur_sum=nums[0]
    max_sum=nums[0]
    #range范围是[1，len(nums)) 左开右闭，切记切记
    for i in range(1,len(nums)):
        #若当前指针指向元素之前的和小于0，则丢弃此元素之前的数列(拖后腿的丢弃！！！)
        #当前和=当前值 与 当前值+之前最大和 的比较中较大的那个、
        #通俗易懂的理解：看当前这个值和之前数列的和，是否会拖当前这个值的后腿，如果扯后腿了说明没必要把之前的数列放到当前和，如果没有扯后腿则把最新的较大数放在当前和里面
        cur_sum=max(nums[i],cur_sum+nums[i])
        #最大和=当前和 与 最大和 的比较中较大的那个
        #通俗易懂的理解：当前和就相当于当前潜在的最大和，把原来的最大和 与当前的潜在最大和进行比较，如果当前和比较大，则更换最大和，否则不更换
        max_sum=max(cur_sum,max_sum)
    return max_sum


nums=[-2,1,-3,4,-1,2,1,-5,4]
'''
  i      cur_sum       max_sum
  0       -2             -2
  1        1              1 
  2       -2              1
  3        4              4
  4        3              4
  5        5              5
  6        6              6
  7        -1             6
  8        3              6
'''

# nums=[-2,1]
print(maxSubArray(nums))


#解法2：动态规划
def maxSubArray_dp(nums):
    # 时间复杂度：O(n),遍历了一遍
    # 空间复杂度:O(1)，几乎没有用其他变量
    for i in  range(1,len(nums)):
        if(nums[i-1]>0):
            nums[i]+=nums[i-1]
    return max(nums)

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray_dp(nums))

#解法3：分治法(题解中拿来的，还不是很懂)
# 连续子序列的最大和主要由这三部分子区间里元素的最大和得到：
# 第 1 部分：子区间 [left, mid]；
# 第 2 部分：子区间 [mid + 1, right]；
# 第 3 部分：包含子区间 [mid , mid + 1] 的子区间，即 nums[mid] 与 nums[mid + 1] 一定会被选取。
def maxSubArray_divide_and_conquer(nums):
    n = len(nums)
    # 递归终止条件
    if n == 1:
        return nums[0]
    else:
        # 递归计算左半边最大子序和
        max_left = maxSubArray_divide_and_conquer(nums[0:len(nums) // 2])
        # 递归计算右半边最大子序和
        max_right = maxSubArray_divide_and_conquer(nums[len(nums) // 2:len(nums)])

    # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
    max_l = nums[len(nums) // 2 - 1]
    tmp = 0
    for i in range(len(nums) // 2 - 1, -1, -1):
        tmp += nums[i]
        max_l = max(tmp, max_l)
    max_r = nums[len(nums) // 2]

    tmp = 0
    for i in range(len(nums) // 2, len(nums)):
        tmp += nums[i]
        max_r = max(tmp, max_r)

    # 返回三个中的最大值
    return max(max_right, max_left, max_l + max_r)


nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray_divide_and_conquer(nums))


# 最大子序和做题总结：
# 贪心，前面的小于0，就丢了。
# 动态规划，前面的元素大于0，就和当前元素相加。
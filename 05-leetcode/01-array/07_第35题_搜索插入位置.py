# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0

#解法1：暴力搜索，头尾特殊判断
def searchInsert_force(nums, target):
    # 特判
    if target in nums:
        return nums.index(target)
    else:
        #特判
        if(nums[0]>target):return 0
        if(nums[-1]<target):return len(nums)

        for i in range(len(nums)):
            if nums[i] < target and nums[i+1]>target:
                return i+1

    # len_count = len(nums)
    # left = 0
    # right = len_count - 1
    # if (target > nums[right]): return len_count
    #
    # while (left < right):
    #     mid = (left + right) // 2
    #     if (target > nums[mid]):
    #         left = mid + 1
    #     else:
    #         right = mid
    #
    # return left

nums=[1,3,5,6]
target=5
print(searchInsert_force(nums, target))

nums=[1,3,5,6]
target=2
print(searchInsert_force(nums, target))

nums=[1,3,5,6]
target=7
print(searchInsert_force(nums, target))

nums=[1,3,5,6]
target=0
print(searchInsert_force(nums, target))

# #解法2：二分查找
# def searchInsert_binary_search(nums, target):
#


# nums=[1,3,5,6]
# target=5
# print(searchInsert_binary_search(nums, target))
#
# nums=[1,3,5,6]
# target=2
# print(searchInsert_binary_search(nums, target))
#
# nums=[1,3,5,6]
# target=7
# print(searchInsert_binary_search(nums, target))
#
# nums=[1,3,5,6]
# target=0
# print(searchInsert_binary_search(nums, target))

#解法一：暴力解法
#不知道为什么IDE上的输出结果和leetdode上的不一样，怀疑是leetcode缺少编译某个环节
def find_num_force(nums1,nums2):
    for i in  range(len(nums2)):
        nums1.append(nums2[i])
    nums1.sort()
    if(len(nums1)%2==0):
        return float((nums1[int(len(nums1)/2-1)]+nums1[int(len(nums1)/2)])/2)
    else:
        return float(nums1[len(nums1)/2])

nums1 = [1, 2]
nums2 = [3, 4]
print(find_num_force(nums1,nums2))


# #解法二：
# def find_num(nums1,nums2):
#
#
# nums1 = [2,3,4]
# nums2 = [3,4,5]
#
# print(find_num(nums1,nums2))
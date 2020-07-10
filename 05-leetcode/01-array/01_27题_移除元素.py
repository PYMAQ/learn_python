
class Car():
    def __init__(self, name, old):
        self.name=name
        self.old=old
    def print(self):
        return print(self.name+'===>'+str(self.old))
    def train(self):
        self.print()
car=Car('Tom', 11)
car.print()
car.train()

class Solution:
    def __init__(self, nums, val):
        self.nums=nums
        self.val=val
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = 0
        j = 0
        while j < length:
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        res = length - (j - i)
        return res
nums = [0,1,2,2,3,0,4,2]
val = 2
sol=Solution(nums,val)
print(nums)
result=sol.removeElement(nums,val)
print(nums)
print(result)

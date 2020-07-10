
nums = [2,7,11,15]
target = 9
#第一种解法：暴力解法
def twoSum_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(target-nums[i]==nums[j]):
                return [i,j]

#第二种解法：字典解法或者叫哈希解法
def twoSum_dict(nums, target):
    hashMap={}
    #按照nums中元素的顺序构造字典，也就是说，下标 和 值 绑定了
    #字典中，只能根据key获取value，而不能根据value获取key(内置的方法中，除非自己实现)
    for key,value in enumerate(nums):
        hashMap[value]=key
    #print(hashMap)
    for key,value in enumerate(nums):
        j=hashMap.get(target-value)
        if((j is not  None)and(key!=j)):
           return [key,j]

#第三种解法：哈希解法升级版，一次循环即可
def twoSum_dict_plus(nums, target):
    hashMap={}
    #字典序遍历nums列表
    #目标值=减数1+减数2

    #key是从0开始，value是对应从0开始的每个nums的值
    for key,value in enumerate(nums):
        #判断减数1是否在字典中，如果在则直接返回结果数组，如果不在则添加进hashmap中
        if(hashMap.get(target-nums[key]) is not  None):
            return [hashMap.get(target-nums[key]),key]
        #如果遍历期间字典中没有这个值则赋值进入。
        hashMap[value]=key

#第四种解法：双指针法
def twoSum_double_pointer(nums, target):

    #复制一个数组
    nums_temp=nums.copy()
    #对数组进行排序，这一步很重要，后面需要排序好的数组
    nums_temp.sort()
    #设置头指针和尾指针
    i=0
    j=len(nums)-1
    #从头扫描 and 从尾扫描
    while(i<j):
        #判断减数1和减数2的和是否大于或者小于目标
        #如果小于目标，则说明头指针要前进
        if nums_temp[i]+nums_temp[j]<target:
            i+=1
        # 如果大于目标，则说明尾指针要后退
        elif nums_temp[i]+nums_temp[j]>target:
            j-=1
        #如果刚好等于目标，则说明达到目标，跳出while循环
        else:
            break
    #此时复制的数组和源数组分离的好处就来了，可以通过复制的数组（已排序好）的减数1的值获取源数组的此值的下标
    i=nums.index(nums_temp[i])
    #【前奏-呼应】pop出去的目的是防止减数1和减数2相等的情况，比如[3,2,3]，[3,3]
    nums.pop(i)
    j=nums.index(nums_temp[j])
    #【后奏-呼应】目的是为了防止减数1和减数2相等的情况
    if(j>=i):
        j+=1
    return [i,j]





list_01=twoSum_force(nums,target)
print(list_01)

list_02=twoSum_dict(nums,target)
print(list_02)

list_03=twoSum_dict_plus(nums,target)
print(list_03)

list_04=twoSum_double_pointer(nums,target)
print(list_04)

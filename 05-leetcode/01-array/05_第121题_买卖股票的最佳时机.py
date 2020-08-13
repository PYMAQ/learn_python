
#解法一：暴力法
def maxProfit(nums):
    max_nums=[]
    if(len(nums)<=1):
        return  0
    for i in range(len(nums)):
        if(i<=len(nums)-2):
            max_nums.append(max(nums[i+1:])-nums[i])
    if(max(max_nums)<0):
        return 0
    else:
        return  max(max_nums)

nums=[7, 1, 5, 3, 6, 4]
#nums=[7,6,4,3,1]
print(maxProfit(nums))

#解法二：动态规划1.0
#  动态规划做题步骤
# 明确 dp(i)dp(i) 应该表示什么（二维情况：dp(i)(j)dp(i)(j)）；
# 根据 dp(i)dp(i) 和 dp(i-1)dp(i−1) 的关系得出状态转移方程；
# 确定初始条件，如 dp(0)dp(0)。

def maxProfit_dp(prices):
    #n是数组长度
    n = len(prices)
    # 边界条件
    if n == 0: return 0
    #dp数组初始化全是0
    dp = [0] * n
    #设定最小值的初试值为股票第一天价格
    minprice = prices[0]

    #从第二天开始遍历
    for i in range(1, n):
        #最小值更新为截止到第i+1天的最低股价
        minprice = min(minprice, prices[i])
        #dp[i]的值为前i天的最大利润
        dp[i] = max(dp[i - 1], prices[i] - minprice)
        print("前"+str(i+1)+'天的最大利润：')
        print(dp[i])
        print(dp)

    return dp[-1]
nums=[7, 1, 5, 3, 6, 4]
#nums=[7,6,4,3,1]
print(maxProfit_dp(nums))



#解法三：动态规划2.0
#假如计划在第 i 天卖出股票，那么最大利润的差值一定是在[0, i-1]之间选最低点买入；
#所以遍历数组，依次求每个卖出时机的的最大差值，再从中取最大值。

#每次可以当天买进，当天卖出，所以最大收益不应该低于0。

# 这种也是动态规划，但是不用维护dp状态机
def maxProfit_once(nums):
    min_priece=int(1e9)
    max_priece=0
    for num in nums:
        #现最高利润=最大值（当前股价-最低股价，原最高利润）
        max_priece=max(num-min_priece,max_priece)
        #现最低利润=最小值（当前股价，原最低利润）
        min_priece=min(num,min_priece)
    return max_priece

nums=[7, 1, 5, 3, 6, 4]
#nums=[7,6,4,3,1]
print(maxProfit_once(nums))




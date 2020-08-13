#暴力超时了
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        v=[]
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                w=abs(j-i)
                h=min(height[i],height[j])
                v.append(w*h)
        # print(v)
        return max(v)

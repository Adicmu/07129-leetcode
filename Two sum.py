class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        r=[]
        m=len(nums)
        for i in range(m):
            l.append(i)
        for i in l:
            for j in l:
                if i!=j:
                    if nums[i]+nums[j]==target:
                        r.append(i) 
                        r.append(j)
                        return r
                

        
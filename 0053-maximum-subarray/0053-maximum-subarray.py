class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
 
        curr=0
        maxi=float('-inf')
        l=len(nums)
        for i in range(l):
            curr+=nums[i]
            maxi=max(maxi,curr)
            if curr<0:
                curr=0
        return maxi
            
            



    

        







        
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        expected= n*(n+1)/2
        actual = expected- sum(nums)
        return actual


        # l=len(nums)
        # for i in range(l+1):
        #     if i not in nums:
        #         # print(i)
        #         return i
        
     
        
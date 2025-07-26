class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#     Kadane’s Algorithm is the optimal solution for finding the maximum subarray sum in an array of integers.

# ✅ Time Complexity: O(n) (single pass through the array)
# ✅ Space Complexity: O(1) (uses only a few variables)
 
        curr=0
        maxi=float('-inf')
        l=len(nums)
        for i in range(l):
            curr+=nums[i]
            maxi=max(maxi,curr)
            if curr<0:
                curr=0
        return maxi
            
            



    

        







        
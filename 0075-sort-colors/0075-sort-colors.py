class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        for i in range(l-1):
            for j in range(i+1, l):
                if nums[i]>nums[j]:
                    nums[i],nums[j]= nums[j], nums[i]
        return nums
    
        
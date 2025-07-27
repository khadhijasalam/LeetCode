class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # 1. Find first decreasing element from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # 2. Find element just bigger than nums[i] on right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # 3. Reverse the part after i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        # sorted is not exactly constant space and time complexity is O(nlogn) compared to O(n) for reverse
        # nums[i + 1:] = sorted(nums[i + 1:])











#############Not completely right:
        # left=0
        # right=len(nums)-1
        # ptr=len(nums)-2
        # temp=[]
        # while left<=right and ptr>=0:
        #     if nums[ptr]<nums[ptr+1]:
        #         left=ptr
        #         nums[ptr],nums[right]= nums[right],nums[ptr]
        #         temp=sorted(nums[left+1:])
        #         # print("temp",temp)
        #         for i in range(len(temp)):
        #             nums[left+1]=temp[i]
        #             left+=1
        #             # print(nums[i])
        #         # print("hello",nums)

        #         return nums          
        #     ptr-=1
        # # print(sorted(nums))
        # return nums.sort()
  

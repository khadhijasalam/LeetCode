class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left=0
        right=len(nums)-1
        res=[0]*len(nums)
        i=len(nums)-1
        print(res)

        while left<=right:
            if abs(nums[left])<abs(nums[right]):
                res[i]=nums[right]**2
                right-=1
                i-=1
            else:
                res[i]=nums[left]**2
                left+=1        
                i-=1
        return res
      

        

        

        
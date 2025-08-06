class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

      
    # First pass: Mark seen numbers by negating the value at the corresponding index
        for i in range(len(nums)):
            index = abs(nums[i]) - 1  # Convert value to index (1-based to 0-based)
            if nums[index] > 0:
                nums[index] *= -1     # Mark as seen by making it negative

        # Second pass: Collect indices that remain positive (i.e., numbers that were not seen)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)  # i+1 is missing since nums[i] is still positive

        return result



        
        # s=set(nums)
        # l=len(nums)
        # ret=[]
        # for i in range(1,l+1):
        #     if i not in s:
        #         ret.append(i)
        # return ret

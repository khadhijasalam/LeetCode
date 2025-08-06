class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=set(nums)
        l=len(nums)
        ret=[]
        for i in range(1,l+1):
            if i not in s:
                ret.append(i)
        return ret

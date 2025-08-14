class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr=nums1.extend(nums2)
        # print(nums1)
        nums1.sort()
        l=len(nums1)
        mid=(l//2)
        if l%2 !=0:  
            return nums1[mid]

        else:
            temp=float((nums1[mid]+nums1[mid-1]))
            return temp/2

        

            
        
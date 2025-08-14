class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        arr=nums1.extend(nums2)
        print(nums1)
      
        nums1.sort()
        # print(nums1)
        l=len(nums1)
        mid=(l//2)
        if l%2 !=0:
            # mid=(l//2)
            print(mid)
            print(nums1[mid])
            return nums1[mid]
            # return nums1[mid]


        else:
            temp=float((nums1[mid]+nums1[mid-1]))

            a=temp/2
            return a

        # print(float(5)/2)
            

            
        
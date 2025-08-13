class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ret=0
        l=0
        r=2
        i=1

        while i< len(arr)-1:
            if arr[i-1]<arr[i]>arr[i+1]:
                l=i-1
                r=i+1

                while l>0 and arr[l-1]<arr[l]:
                    l-=1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                
                ret= max(ret,r-l+1)
                i=r
            i+=1
        return ret

    
            
        
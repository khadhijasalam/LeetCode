class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        # Optimal
        left=0
        mid=0
        right=l-1
        while mid<=right:
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                mid+=1
                left+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1
        return nums
            
            




        #Better
   
        # count=[0,0,0]
        # for i in nums:
        #     if i==0:
        #         count[0]+=1
        #     elif i ==1:
        #         count[1]+=1
        #     else:
        #         count[2]+=1
        # print(count)
        # c_red=0
        # c_white=0
        # # c_blue=
        # for i in range(l):
        #     if c_red != count[0]:
        #         nums[i]=0
        #         c_red+=1
                
        #     elif c_white!= count[1]:
        #         nums[i]=1
        #         c_white+=1
              
        #     else:
        #         nums[i]=2
        # return nums



        #Brute
             # for i in range(l-1):
        #     for j in range(i+1, l):
        #         if nums[i]>nums[j]:
        #             nums[i],nums[j]= nums[j], nums[i]
        # return nums
            
            
            

    
        
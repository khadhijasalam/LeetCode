class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # ans=set()
      
        # l=len(nums)
        # for i in range(l-2):
        #     for j in range(i+1,l-1):
        #         for k in range(j+1,l):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 a=[nums[i],nums[j],nums[k]]
        #                 triplet= tuple(sorted(a))
        #                 if triplet not in ans:
        #                     ans.add(triplet)
                       
        # return list(ans)

        # ans=[]
        # l=len(nums)
        # nums.sort()
        # left=0
        # right=l-1
        # ptr=1

        # while right<l :
        #     sumi=nums[left]+nums[ptr]+nums[right]
        #     if sumi==0 and left!=right and right!=ptr:
        #         a=[nums[left],nums[ptr],nums[right]]
        #         ans.append(a)
        #         left+=1
        #         right-=1
                
        #     elif sumi>0:
        #         right-=1
        #     elif sumi<0:
        #         left+=1
          
        # return ans


        nums.sort()
        ans=[]
        print(nums)
        
        for fixed in range(0,len(nums)-2):
            left=fixed+1
            right=len(nums)-1
            
            if fixed>0 and nums[fixed]==nums[fixed-1]:
                continue
            while left<right:
                sumi=nums[fixed]+nums[left]+nums[right]
               
                if sumi<0:
                    left+=1
                elif sumi>0:
                    right-=1
                else:
                    ans.append([nums[fixed],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                
                    
                
            
        return ans
            



            

        
            

        
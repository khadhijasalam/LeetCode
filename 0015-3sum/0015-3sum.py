class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ####
        # Hashing
        #####
        nums.sort()  # Sorting helps handle duplicates
        res = set()
        l = len(nums)

        for i in range(l):
            hash_set = set()
            for j in range(i+1, l):
                k = -(nums[i] + nums[j])
                if k in hash_set:
                    triplet = tuple(sorted([nums[i], nums[j], k]))
                    res.add(triplet)
                hash_set.add(nums[j])

        return [list(t) for t in res]
            



        # i=0
        # j=1
        # hash=set()
        # res=set()
        # l=len(nums)
    
        # nums.sort()
        # for i in range(l):
        #     hash=set()
        #     for j in range(i+1,l):
                
        #         k=-(nums[i]+nums[j])    #arr[i]+arr[j]+arr[k]=0. Bring other side
        #         print(k)
        #         if k in hash:
        #             temp=[nums[i],nums[j],k]
        #             res.add(tuple(temp))
        #             # print(res)
        #         hash.add(nums[j])

        #         # else:
        #         #     hash.add(k)
        # return list(res)



        # Doesnt work cause it give duplicat. so add in set as tuple then convert to lis
        # res=[]
        # l=len(nums)
        # for i in range(l):
        #     for j in range(i+1,l):
        #         for k in range(j+1,l):
        #             if nums[i]+nums[j]+nums[k]==0 and (i != j and i != k and j != k):
                        
        #                 res.append([nums[i],nums[j],nums[k]])
        # print(res)
        # return res

        ##################### Error:
        # left=0
        # right=len(nums)-1
        # i=1
        # res=[]
        # while left<=right and i<=right:
        #     curr_val=nums[left]+nums[i]+nums[right]
        #     if curr_val==0:
        #         res.append([nums[i],nums[left],nums[right]])
        #     if i==right:
        #         right-=1
        #         i=left+1
        #     i+=1
        # print(res)
            


        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr=head
        # count=0
        # while curr is not None:
        #     # print(curr.val)
        #     count+=1
        #     curr=curr.next
        #     # print(count)
        # if count%2==0:
        #     mid= int((count/2 )+1)
        # else: 
        #     mid=ceil(count/2)
        # # print(mid)
        # c=0
        # curr=head
        # # ans=[]
        # while curr is not None:
        #     # print(curr.val)
        #     c+=1
        #     if c==mid:
        #         # ans.append(curr.val)
        #         return curr
            
        #     curr=curr.next


        #OPTIMAL:When fast reaches the end, slow will be at the middle. because fast is twice as fastas slow

        slow = head
        fast = head
        
        # Move fast 2x as quickly as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast reaches end, slow is in middle
        return slow
     

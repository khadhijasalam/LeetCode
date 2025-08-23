from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=deque()
        curr=head
        while curr is not None:
            stack.append(curr.val)
            
            curr=curr.next
        curr=head
        while stack:
            curr.val=stack.pop()
            curr=curr.next
            # print(curr)

        return head


       
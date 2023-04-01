# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        n = head
        while n:
            cnt += 1
            n = n.next
        
        cnt = cnt // 2
        
        a = head
        while cnt:
            cnt -= 1
            a = a.next
        
        return a
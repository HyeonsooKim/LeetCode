# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0)
        total=0
        r=ListNode(0,d)
        while head:
            if head.val:
                total+=head.val
            else:
                if total:
                    d.next=ListNode(total)
                    d=d.next
                    total=0
            head=head.next
        return r.next.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        vals = []
        while cur:
            vals.append(cur.val)
            cur = cur.next
        vals.sort()
        cur = head
        i = 0
        while cur:
            cur.val = vals[i]
            i+=1
            cur = cur.next
        return head
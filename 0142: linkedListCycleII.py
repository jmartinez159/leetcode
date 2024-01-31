# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointers = set()
        curr = head
        while curr:
            if curr in pointers:
                return curr
            else:
                pointers.add(curr)
                curr = curr.next
        return None
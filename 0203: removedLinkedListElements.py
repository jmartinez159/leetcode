# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(next=head)
        prev = ans
        current = head
        while current is not None:
            nxt = current.next
            if current.val == val:
                prev.next = nxt
            else:
                prev = current
            current = nxt
        return ans.next
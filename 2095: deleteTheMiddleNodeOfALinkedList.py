# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        if len(nodes) == 1:
            return None
        removeNode = len(nodes)//2
        cur = nodes[removeNode-1]
        cur.next = nodes[removeNode].next
        return head
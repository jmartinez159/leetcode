# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointMap = {}
        current = headA
        while current is not None:
            pointMap[current] = 1 + pointMap.get(current, 0)
            current = current.next
        current = headB
        while current is not None:
            if current in pointMap:
                return current
            current = current.next
        return None
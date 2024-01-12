# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        points = []
        while current is not None:
            count+=1
            points.append(current)
            current = current.next
        stop = int(count/2)
        return points[stop]
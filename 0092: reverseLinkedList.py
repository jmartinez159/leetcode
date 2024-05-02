# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        left -=1
        right -=1
        pList = []
        cur = head

        while cur:
            pList.append(cur)
            cur = cur.next

        stack = []
        ans = ListNode(0)
        cur = ans
        for i in range(left,right+1):
            stack.append(pList[i])

        for i in range(len(pList)):
            if i >= left and i <= right:
                cur.next = stack.pop()
            else:
                cur.next = pList[i]
            cur = cur.next
        cur.next = None
        
        return ans.next
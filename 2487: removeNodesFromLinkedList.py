# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        stack = []
        maxVal = 0
        for i in range(len(nodes)):
            if maxVal <= nodes[len(nodes)-1-i].val:
                maxVal = nodes[len(nodes)-1-i].val
                stack.append(nodes[len(nodes)-1-i])

        res = ListNode(0)
        curr = res
        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        
        return res.next
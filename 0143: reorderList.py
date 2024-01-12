# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pointers = []
        current = head
        while current is not None:
            pointers.append(current)
            current = current.next
        i = 1
        n = len(pointers)-1
        current = head
        while i < n:
            current.next = pointers[n]
            current = current.next
            current.next = pointers[i]
            current = current.next
            i+=1
            n-=1
        if i == n:
            pointers[i].next = None
            current.next = pointers[i]
        else:
            current.next = None
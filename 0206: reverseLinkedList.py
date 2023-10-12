# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        lst = []
        while cur != None:
            lst.append(cur.val)
            cur = cur.next
        lst = lst[::-1]
        count = len(lst)
        cur = head
        i = 0
        while cur != None:
            cur.val = lst[i] 
            cur = cur.next
            i = i +1
        return head
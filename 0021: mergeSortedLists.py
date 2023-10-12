# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = []
        cur = list1
        while cur != None:
            ans.append(cur.val)
            cur = cur.next
        cur = list2
        while cur != None:
            ans.append(cur.val)
            cur = cur.next
        ans.sort()
        cur = None
        head = None
        for x in ans:
            if head == None:
                head = ListNode(x)
                cur = head
            else:
                cur.next = ListNode(x)
                cur = cur.next
        return head
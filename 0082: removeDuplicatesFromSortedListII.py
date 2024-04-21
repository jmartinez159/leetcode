# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        freqNum = {}
        res = []
        curr = head
        while curr:
            freqNum[curr.val] = freqNum.get(curr.val, 0)+1
            curr = curr.next
        
        for key in freqNum.keys():
            if freqNum[key] == 1:
                res.append(key)

        res.sort()
        ans = ListNode(0)
        curr = ans
        for i in res:
            curr.next = ListNode(i)
            curr = curr.next
        return ans.next
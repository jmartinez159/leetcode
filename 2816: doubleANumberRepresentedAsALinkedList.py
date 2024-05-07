# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = []
        curr = head
        while curr:

            num.append(curr.val)
            curr = curr.next
            
        stack = []
        carry = 0
        for i in range(len(num)):
            temp = 2*num[len(num)-1-i]+carry
            carry = temp//10
            temp = temp%10
            stack.append(temp)
        if carry == 1:
            stack.append(carry)

        res = ListNode(0)
        curr = res
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        
        return res.next
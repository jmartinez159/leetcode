# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] != nums[j]:
                return False
            i+=1
            j-=1
        return True
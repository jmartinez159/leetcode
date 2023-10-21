class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits)-1
        carry = 1
        while j >= 0:
            digits[j] += carry
            carry = 0
            if digits[j] >= 10 and j == 0:
                digits[j] = 1
                digits.append(0)
            elif digits[j] >= 10:
                digits[j] = 0
                carry = 1
            j-=1
        return digits
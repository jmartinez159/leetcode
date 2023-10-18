class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        k = len(numbers)-1
        while i < k:
            curSum = numbers[i] + numbers[k]
            if curSum > target:
                k -=1
            if curSum < target:
                i+=1
            if curSum == target:
                return [i+1,k+1]
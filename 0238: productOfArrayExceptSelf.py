class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        indexZero = -1
        zeroCount = 0
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
                indexZero = i
            else:
                product = product * nums[i]
        
        if zeroCount > 1:
            for i in range(len(nums)):
                nums[i] = 0
            return nums
        
        if zeroCount == 1:
            for i in range(len(nums)):
                if i == indexZero:
                    nums[i] = product
                else:
                    nums[i] = 0
            return nums

        for i in range(len(nums)):
            nums[i] = product//nums[i]
        return nums
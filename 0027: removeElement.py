class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = []
        for x in nums:
            if x != val:
                res.append(x)
        k = len(res)
        i = 0
        while i < k:
            nums[i] = res[i]
            i+=1
        return k
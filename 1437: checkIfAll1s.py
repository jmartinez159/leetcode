class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indices = []
        i = 0
        for x in nums:
            if x == 1:
                indices.append(i)
            i+=1
        prev = None
        for x in indices:
            if prev == None:
                prev = x
                continue
            print(x - prev)
            if (x - prev-1) < k:
                return False
            prev = x
        return True
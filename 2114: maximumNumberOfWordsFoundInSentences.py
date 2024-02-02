class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for string in sentences:
            count = 1
            for char in string:
                if char.isalpha():
                    continue
                count +=1
            res = max(res, count)
        return res
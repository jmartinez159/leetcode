class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqs = {}
        checker = set()
        for x in arr:
            freqs[x] = freqs.get(x, 0) +1
        for x in freqs.values():
            checker.add(x)
        return len(freqs.values()) == len(checker)
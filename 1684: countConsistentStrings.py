class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        validSet = set()
        ans = 0
        for x in allowed:
            validSet.add(x)

        for w in words:
            ans+=1
            for c in w:
                if c not in validSet:
                    ans-=1
                    break           
        return ans
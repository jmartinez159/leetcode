class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        m = {}
        for x in strs:
            index = ''.join(sorted(x))
            if index not in m:
                m[index] = []
            m[index].append(x)

        for x in m.keys():
            cur = []
            for y in range(len(m[x])):
                cur.append(m[x][y])
            ans.append(cur)
        return ans
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = []
        for i in score:
            ranks.append(i)
        
        ranks.sort()
        rankMap = {}
        for i in range(len(ranks)):
            curr = ranks[len(ranks)-1-i]
            if i == 0:
                rankMap[curr] = "Gold Medal"
            elif i == 1:
                rankMap[curr] = "Silver Medal"
            elif i == 2:
                rankMap[curr] = "Bronze Medal"
            else:
                rankMap[curr] = str(i+1)
        
        res = []
        for i in score:
            res.append(rankMap[i])
        return res
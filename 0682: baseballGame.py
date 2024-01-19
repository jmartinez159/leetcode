class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        ops = "+DC"
        for x in operations:
            if x in ops:
                if x == "C":
                    score.pop()
                elif x == "D":
                    score.append(score[-1]*2)
                elif x == "+":
                    score.append(score[-1]+score[-2])
            else:
                score.append(int(x))
        return sum(score)
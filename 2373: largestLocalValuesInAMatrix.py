class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        limit = n-2
        res = []
        for i in range(limit):
            res.append([])
            for j in range(limit):
                currMax = grid[i][j]
                for x in range(3): 
                    for y in range(3):
                        currMax = max(currMax, grid[i+x][j+y])
                res[i].append(currMax)

        return res
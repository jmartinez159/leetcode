class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # check for rotting oranges
        indexQ = deque()
        freshOranges = 0
        res = -1
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    indexQ.append((row,col))
                if grid[row][col] == 1:
                    freshOranges += 1

        if freshOranges == 0:
            return 0
        # check for any adjacent fresh oranges
        while indexQ:
            for i in range(len(indexQ)):
                x,y = indexQ.popleft()
                if x-1 >= 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    indexQ.append((x-1,y))

                if y+1 < n and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    indexQ.append((x,y+1))

                if x+1 < m and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    indexQ.append((x+1,y))

                if y-1 >= 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    indexQ.append((x,y-1))
            res += 1
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1
        return res
        # update table and repeat step 1

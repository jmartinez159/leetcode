class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        queue = deque()
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    continue
                if (row,col) in visited:
                    continue
                queue.append((row,col))
                curArea = 0
                while queue:
                    ro, co = queue.popleft()
                    if (ro,co) in visited:
                        continue
                    curArea += 1
                    visited.add((ro,co))
                    if ro-1 >= 0 and grid[ro-1][co] == 1:
                        queue.append((ro-1, co))

                    if ro+1 < ROWS and grid[ro+1][co] == 1:
                        queue.append((ro+1, co))

                    if co-1 >= 0 and grid[ro][co-1] == 1:
                        queue.append((ro, co-1))

                    if co+1 < COLS and grid[ro][co+1] == 1:
                        queue.append((ro, co+1))
                
                res = max(res, curArea)
        return res
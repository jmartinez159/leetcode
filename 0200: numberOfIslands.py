class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        checked = set()
        queue = deque()
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '0':
                    continue
                if (row,col) in checked:
                    continue
                queue.append((row,col))
                res += 1
                while queue:
                    ro,co = queue.popleft()
                    if (ro,co) in checked:
                        continue
                    checked.add((ro,co))
                    if ro-1 >= 0 and grid[ro-1][co] == '1':
                        queue.append((ro-1, co))

                    if ro+1 < ROWS and grid[ro+1][co] == '1':
                        queue.append((ro+1, co))

                    if co-1 >= 0 and grid[ro][co-1] == '1':
                        queue.append((ro, co-1))

                    if co+1 < COLS and grid[ro][co+1] == '1':
                        queue.append((ro,co+1))
        return res
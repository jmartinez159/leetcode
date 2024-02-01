class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOrange = 0
        queueRot = deque()
        ROWS, COLS = len(grid), len(grid[0])
        res = -1
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queueRot.append((row,col))
                if grid[row][col] == 1:
                    freshOrange += 1

        if freshOrange == 0:
            return 0
        
        while queueRot:
            res += 1
            for i in range(len(queueRot)):
                ro, co = queueRot.popleft()
                
                if ro-1 >= 0 and grid[ro-1][co] == 1:
                    freshOrange -= 1
                    grid[ro-1][co] = 2
                    queueRot.append((ro-1, co))
                
                if ro+1 < ROWS and grid[ro+1][co] == 1:
                    freshOrange -= 1
                    grid[ro+1][co] = 2
                    queueRot.append((ro+1, co))

                if co-1 >= 0 and grid[ro][co-1] == 1:
                    freshOrange -= 1
                    grid[ro][co-1] = 2
                    queueRot.append((ro, co-1))

                if co+1 < COLS and grid[ro][co+1] == 1:
                    freshOrange -= 1
                    grid[ro][co+1] = 2
                    queueRot.append((ro, co+1))
        if freshOrange > 0:
            return -1
        return res
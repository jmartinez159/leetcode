class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        notValid = set()
        queueO = deque()
        ROWS, COLS = len(grid), len(grid[0])
        #checking edges for Os
        for col in range(COLS):
            if grid[0][col] == 'O':
                queueO.append((0, col))
            if grid[ROWS-1][col] == 'O':
                queueO.append((ROWS-1, col))
        for row in range(ROWS):
            if grid[row][0] == 'O':
                queueO.append((row, 0))
            if grid[row][COLS-1] == 'O':
                queueO.append((row, COLS-1))
        while queueO:
            ro, co = queueO.popleft()
            if (ro,co) in notValid:
                continue
            notValid.add((ro, co))
            if ro-1 >= 0 and grid[ro-1][co] == 'O':
                queueO.append((ro-1, co))

            if ro+1 < ROWS and grid[ro+1][co] == 'O':
                queueO.append((ro+1, co))

            if co-1 >= 0 and grid[ro][co-1] == 'O':
                queueO.append((ro, co-1))

            if co+1 < COLS and grid[ro][co+1] == 'O':
                queueO.append((ro, co+1))
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 'O' and (row,col) not in notValid:
                    grid[row][col] = 'X'
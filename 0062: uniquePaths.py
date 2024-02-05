class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def traverse(row,col):
            key = str(row) + ',' + str(col)
            if key in memo:
                return memo[key]
            if row == 0 or col == 0:
                return 0
            if row == 1 and col == 1:
                return 1

            memo[key] = traverse(row-1, col) + traverse(row, col-1)
            return memo[key]
        return traverse(m,n)
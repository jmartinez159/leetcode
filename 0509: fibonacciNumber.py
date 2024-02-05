class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        def fibo(n):
            if n in memo:
                return memo[n]
            if n <= 2:
                return 1
            memo[n] = fibo(n-1) + fibo(n-2)
            return memo[n]
        return fibo(n)
class Solution {
public:

    map<int,int> memo;

    int climbStairs(int n) {
        
        if(memo.contains(n))
            return memo[n];

        if(n == 0)
            return 1;

        if(n < 0)
            return 0;

        memo[n] = climbStairs(n-1)+climbStairs(n-2);
        return memo[n];
    }
};
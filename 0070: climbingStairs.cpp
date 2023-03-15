class Solution {
public:
    int climbStairs(int n) {

        int len = 2;
        int a = 1, b = 1;
        while(n >= len){

            int c = a + b;
            a = b;
            b = c;
            len++;
        }

        return b;
    }
};

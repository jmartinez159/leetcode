class Solution {
public:
    int tribonacci(int n) {
        
        int a = 0;
        int b = 1;
        int c = 1;
        int res = 0;
        if(n == 1 || n == 2){

            return 1;
        }

        for(int i = 3; i < n+1; i++){

            res = a+b+c;
            a = b;
            b = c;
            c = res;
        }

        return res;
    }
};
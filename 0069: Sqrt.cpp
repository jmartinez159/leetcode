class Solution {
public:
    int mySqrt(int x) {
        
        if(x == 0 || x == 1){

            return x;
        }

        long long ans = 2;    
        while(ans*ans != x){

            if(ans*ans > x){

                return ans-1;
            }
            ans++;
        }

        return ans;
    }
};

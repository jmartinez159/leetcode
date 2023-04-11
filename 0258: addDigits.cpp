//problem : https://leetcode.com/problems/add-digits/description/

class Solution {
public:
    int addDigits(int num) {
        
        int ans = 0;
        while(true){

            while(num > 0){

                ans = ans + (num%10);
                num = num/10; 
            }
            
            if(ans > 9){

                num = ans;
                ans = 0;
            }
            else{

                return ans;
            }
        }
        

        return ans;
    }
};

// problem : https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

class Solution {
public:
    int arraySign(vector<int>& nums) {
        
        bool neg = false;
        for(int i  = 0; i < nums.size(); i++){

            if(nums[i] == 0){

                return 0;
            }

            if(nums[i] < 0){

                flip(neg);
            }
        }

        if(neg){

            return -1;
        }

        return 1;


    }

    void flip(bool &x){

        if(x){

            x = false;
        }
        else{

            x = true;
        }
        
    }


};

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        vector<int> ans(nums.size()+1, 0);    //vector of size n with all 0s
        for(int i = 0; i < nums.size(); i++){

            ans[nums[i]]++;
        }

        for(int i = 0; i < ans.size(); i++){

            if(ans[i] == 0){

                return i;
            }
        }

        return 0;
    }
};

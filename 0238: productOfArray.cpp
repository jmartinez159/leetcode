class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prod = 1;
        int zindex = 0;
        int zcount = 0;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i]==0){
                zcount++;
                zindex = i;
                continue;
            }
            prod *= nums[i];
        }

        if(zcount > 1){

            return vector<int>(nums.size(), 0);
        }

        if(zcount > 0){

            vector<int> ans(nums.size(), 0);
            ans[zindex] = prod;
            return ans;
        }

        for(int i = 0; i < nums.size(); i++){

            nums[i] = prod/nums[i];
        }

        return nums;
    }
};
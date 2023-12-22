class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        vector<bool> check(nums.size()+1, false);
        for(int i = 0; i < nums.size(); i++){

            if(check[nums[i]]){

                return nums[i];
            }
            else{

                check[nums[i]] = true;
            }
        }

        return 0;
    }
};
class Solution {
public:
    int findMaxK(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        int i = 0;
        int j = nums.size()-1;
        while(i < j){

            if(nums[i] > 0 || nums[j] < 0){

                break;
            }

            if(abs(nums[i]) == nums[j]){

                return nums[j];
            }

            if(abs(nums[i]) < nums[j]){

                j--;
            }

            else{

                i++;
            }
        }

        return -1;
    }
};
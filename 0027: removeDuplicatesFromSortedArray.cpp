class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        if(nums.empty()){

            return 0;
        }

        int k = 1;
        int current = nums[0];
        for(int i = 1; i < nums.size(); i++){

            if(current != nums[i]){

                nums[k] = nums[i];
                current = nums[i];
                k++;
            }
        }

        return k;
    }
};

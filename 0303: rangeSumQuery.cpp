class NumArray {
public:

    int *array = nullptr;

    NumArray(vector<int>& nums) {

        array = new int[nums.size()];
        for(int i = 0; i < nums.size(); i++){

            array[i] = nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        int ans = 0;
        for(int i = left; i <= right; i++){
            ans += array[i];
        }
        return ans;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
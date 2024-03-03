class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        priority_queue<int> ans;
        for(int i = 0; i < nums.size(); i++){

            ans.push(nums[i]*nums[i]);
        }

        int i = nums.size()-1;
        while(!ans.empty()){
            nums[i] = ans.top();
            ans.pop();
            i--;
        }

        return nums;
    }
};
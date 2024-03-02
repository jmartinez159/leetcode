class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        priority_queue<int> maxHeap;
        if(nums.size() == 1){

            return nums[0];
        }

        for(int i = 0; i < nums.size(); i++){

            maxHeap.push(nums[i]);
        } 

        int res = maxHeap.top();
        while(!maxHeap.empty() && k > 1){
            maxHeap.pop();
            res = maxHeap.top();
            k--;
        }

        return res;
    }
};
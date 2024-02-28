class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int low = 0;
        int high = nums.size()-1;
        int mid = 0;
        while(low <= high){
            mid = (low+high)/2;
            if((mid < nums.size()-1) && (nums[mid] < nums[mid+1])){
                low++;
            }

            else if((mid > 0) && (nums[mid]) < nums[mid-1]){
                high--;
            }
            else{
                break;
            }
        }
        return mid;
    }
};
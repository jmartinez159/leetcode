// problem : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        
        vector<int> ans(100001, 0);
        vector<int> sol;
        for(int i = 0; i < nums.size(); i++){

            ans[nums[i]-1]++;
        }

        for(int i = 0; i < nums.size(); i++){

            if(ans[i] == 0){

                sol.push_back(i+1);
            }
        }

        return sol;

    }
};

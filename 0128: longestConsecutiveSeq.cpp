class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> ans;
        for(int i = 0; i < nums.size(); i++){

            ans.insert(nums[i]);
        }
        int streakMax = 0;
        int streak = -1;
        int prev;
        for(auto it : ans){

            if(streak ==-1){

                streak = 1;
                prev = it;
                continue;
            }

            if(prev+1 == it){

                streak++;
            }
            else{

                if(streak > streakMax){

                    streakMax = streak;
                }

                streak = 1;
            }
            prev = it;
        }

        if(streak > streakMax){

            streakMax = streak;
        }

        return streakMax;
    }
};
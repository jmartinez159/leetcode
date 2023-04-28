// problem : https://leetcode.com/problems/intersection-of-two-arrays/description/

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        
        map<int, int> map;
        set<int> order;
        vector<int> ans;
        for(int i = 0; i < nums1.size(); i++){

            map[nums1[i]]++;
        }

        for(int i = 0; i < nums2.size(); i++){

            if(map[nums2[i]] != 0){

                //cout << nums2[i] << endl;
                order.insert(nums2[i]);
            }
        }


        for(auto it : order){

            ans.push_back(it);
        }
        return ans;
    }
};

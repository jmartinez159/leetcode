class Solution {
public:

    map<string, int> map;

    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        
        return solve(nums1, nums2, 0, 0);
    }

    int solve(const vector<int>& a, const vector<int>& b, int ai, int bi){

            if(ai == a.size() || bi == b.size()){

            return 0;
        }

        string s = to_string(ai) + " " + to_string(bi);

        if(map.count(s)){

            return map[s];
        }

        if(a[ai] == b[bi]){

           map[s] = solve(a, b, ai+1, bi+1) +1;
           return map[s];
        }

        int s1 = solve(a, b, ai+1, bi);
        int s2 = solve(a, b, ai, bi+1);
        map[s] = max(map[s], max(s1, s2));

        return map[s];
    }
};

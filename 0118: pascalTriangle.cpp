class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
        vector<vector<int>> ans;
        
        for(int i = 0; i < numRows; i++){

            vector<int> temp(i+1);
            temp[0] = 1;
            temp[i] = 1;
            for(int k = 1; k < i; k++){

                temp[k] = ans.back()[k-1] + ans.back()[k];
            }

            ans.push_back(temp);
        }

        return ans;
        
    }
};

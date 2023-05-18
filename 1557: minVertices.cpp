// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/

class Solution {
public:

    vector<int> check;
    vector<vector<int>> table;

    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {

        vector<int> checker(n, 0);
        vector<int> ans;
        for(int i = 0; i < edges.size(); i++){

            checker[edges[i][1]] = 1;
        }

        for(int i = 0; i < n; i++){

            if(checker[i] == 0){

                ans.push_back(i);
            }
        }

        return ans;
    }

};

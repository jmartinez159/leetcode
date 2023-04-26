// problem : https://leetcode.com/problems/zigzag-conversion/description/

class Solution {
public:
    string convert(string s, int numRows) {
        
        if(numRows == 1){

            return s;
        }

        vector<string> ans;
        string sol;
        for(int i = 0; i < numRows; i++){

            ans.push_back("");
        }

        int index = 0;
        bool zz = true;
        for(int i = 0; i < s.size(); i++){

            ans[index]+= s[i];
            if(index == numRows-1){

                zz = false;
            }

            if(index == 0){

                zz = true;
            }

            if(zz){

                index++;
            }

            else{

                index--;
            }
        }

        for(int i = 0; i < numRows; i++){

            sol += ans[i];
        }

        return sol;
    }
};

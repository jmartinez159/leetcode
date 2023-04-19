// problem : https://leetcode.com/problems/is-subsequence/description/

class Solution {
public:
    bool isSubsequence(string s, string t) {
        
        if(s.size() > t.size()){

            return false;
        }

        int i = 0;
        int k = 0;
        while(k < t.size()){

            if(i == s.size()){

                return true;
            }

            if(s[i] == t[k]){

                i++;
            }
            
            k++;
        }

        if(i == s.size()){

                return true;
        }

        return false;
    }
};

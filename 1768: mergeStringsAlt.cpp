// problem : https://leetcode.com/problems/merge-strings-alternately/description/

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        
        string ans = "";
        int i = 0;
        int k = 0;
        while(i < word1.size() && k < word2.size()){

            ans += word1[i];
            ans += word2[k];
            i++;
            k++;
        }

        while(i < word1.size()){

            ans += word1[i++];
        }

        while(k < word2.size()){

            ans += word2[k++];
        }
        return ans;
    }
};

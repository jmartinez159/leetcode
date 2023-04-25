// problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        unordered_map<char, int> map;
        int max = 0;
        for(int i = 0; i < s.size(); i++){
            map[s[i]]++;
            for(int k = i+1; k < s.size(); k++){


                if(map[s[k]] != 0){

                    break;
                }

                map[s[k]]++;
            }

            if(max < map.size()){

                max = map.size();
            }

            map.clear();
        }

        return max;
    }
};

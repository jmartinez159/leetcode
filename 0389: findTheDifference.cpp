//problem : https://leetcode.com/problems/find-the-difference/description/

class Solution {
public:
    char findTheDifference(string s, string t) {
        
        map<char, int> map;
        for(int i =0; i < s.size(); i++){

            map[s[i]]++; 
        }

        for(int i = 0; i < t.size(); i++){

            if(map.find(t[i]) == map.end()){

                return t[i];
            }
            map[t[i]]--;
        }

        for(auto it : map){

            if(it.second != 0){

                return it.first;
            }
        }

        return 'x';
    }
};

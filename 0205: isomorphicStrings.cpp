class Solution {
public:



    bool isIsomorphic(string s, string t) {
        
        unordered_map<char, char> ans;
        unordered_set<char> used;

        for(int i = 0; i < s.size(); i++){

            char c1 = s[i];
            char c2 = t[i];
            if(ans.count(c1) == 0){

                if(used.count(c2)){

                    return false;
                }
                
                ans[c1] = c2;
                used.insert(c2);
            }
            else{

                char current = ans[c1];
                if(current != c2){

                    return false;
                }

            }
        }

        return true;
    }


};

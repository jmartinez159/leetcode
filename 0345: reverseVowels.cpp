class Solution {
public:
    string reverseVowels(string s) {
        
        vector<int> indx;
        vector<char> vows;
        string check = "AEIOUaeiou";
        for(int i = 0; i < s.size(); i++){

            if(check.find(s[i]) != -1){
                indx.push_back(i);
                vows.push_back(s[i]);
            }
        }

        for(int i = 0; i<indx.size(); i++){

            int cur = indx.size()-1-i;
            s[indx[cur]] = vows[i];
        }

        return s;
    }
};
class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.size() != t.size()){

            return false;
        }

        vector<int> letters;
        for(int i = 0; i < 26; i++){

            letters.push_back(0);
        }

        for(int i = 0; i < s.size(); i++){

            int index = s[i] - 97;
            letters[index]++;
            index = t[i] - 97;
            letters[index]--;
        }

        for(int i = 0; i < letters.size(); i++){

            if(letters[i] != 0){

                return false;
            }
        }

        // char c = letters.size()-1 +97;
        // cout << endl << c <<endl;

        return true;
    }
};

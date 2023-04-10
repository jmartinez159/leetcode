class Solution {
public:
    string reverseVowels(string s) {
        
        string v = "AEIOUaeiou";
        int i = 0;
        int k = s.size()-1;
        while(i < k){

            int index = v.find(s[i]);
            if(index != -1){

                while(true){

                    if(v.find(s[k]) != -1 || i == k){

                        break;
                    }

                    k--;
                }
                
                char c = s[i];
                s[i] = s[k];
                s[k] = c;
                k--;
            }
            i++;
        }

        return s;
    }
};

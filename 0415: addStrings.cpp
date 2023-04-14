//Problem : https://leetcode.com/problems/add-strings/description/

class Solution {
public:
    string addStrings(string num1, string num2) {
        
        int i = num1.size()-1, k = num2.size()-1;

        string ans = "";

        while(i >= 0 && k >= 0){

            char c1 = (num1[i--] + num2[k--]) - 48;

            ans += c1;
        }

        while(k >= 0){

            // ans.insert(0,1, );
            ans += num2[k--];
        }

        while(i >= 0){

            // ans.insert(0,1, );
            ans += num1[i--];
        }

        for(int i = 0; i < ans.size(); i++){

            // - '0'
            if(ans[i] > '9'){

                ans[i] -= 10;

                if(i+1 < ans.size()){

                    ans[i+1] += 1;
                }

                else{

                    ans += '1';
                }
                
            }
        }

        reverse(ans.begin(), ans.end());

        return ans;
    }
};

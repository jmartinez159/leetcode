class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int count1 = 0;
        int count0 = 0;
        string ans = "";
        for(int i = 0; i < s.size(); i++){

            if(s[i] == '1'){
                count1++;
            }
            else{
                count0++;
            }
        }

        while(count1 > 1){

            ans += "1";
            count1--;
        }
        while(count0 > 0){
            ans += "0";
            count0--;
        }
        if(count1 == 1){
            ans += '1';
        }
        return ans;
    }
};
class Solution {
public:
    int secondHighest(string s) {
        
        vector<bool> chart(10, false);
        for(int i = 0; i < s.size(); i++){

            if(s[i] >= 48 && s[i] <= 57){
                cout << s[i] <<endl;
                chart[s[i]-48] = true;
            }
        }

        int count = 0;
        for(int i = 9; i >= 0; i--){

            if(chart[i]){

                if(count ==0){
                    count++;
                }
                else{
                    return i;
                }
            }
        }

        return -1;
    }
};
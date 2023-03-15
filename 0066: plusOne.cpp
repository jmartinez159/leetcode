class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        int carry = 1;
        for(int i = 0; i < digits.size(); i++){

            int index = digits.size()-1-i;
            digits[index] += carry;
            carry = 0; //reset 
            if(digits[index] == 10){

                digits[index] = 0;
                carry = 1;
            }
            
            if(index == 0 && carry == 1){

                digits.insert(digits.begin(), 1);
                break;
            }
          
        }

        return digits;
    }
};

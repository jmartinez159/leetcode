class Solution {
public:
    int singleNumber(vector<int>& nums) {

        int *counts = new int[60002];
        for(int i = 0; i < 60001; i++){

            counts[i] = 0;
        }

        int index; 
        for(int i = 0; i < nums.size(); i++){

            index = nums[i];
            if(index < 0){

                index *= -1;
            }

            else if(index > 0){

                index += 30001;
            }

            counts[index]++;              
        }

        for(int i = 0; i < 60002; i++){

            if(counts[i] == 1){

                if(i < 30001){

                    return i*-1;
                }
                else{

                    return i-30001;
                }
            }
        }

        return 0;
    }
};

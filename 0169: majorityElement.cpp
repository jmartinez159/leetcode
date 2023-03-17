class Solution {
public:
    
    vector<int> list;
    vector<int> counts;

    int majorityElement(vector<int>& nums) {

        if(nums.size() == 1){

            return nums[0];
        }
        
        int index;
        for(int i = 0; i < nums.size(); i++){

            //cout << i << endl;
            index = find(nums[i]);
            if(index > -1){

                counts[index] += 1;
                if(counts[index] > (nums.size()/2)){

                    return list[index];
                }
            }

            else{

                list.push_back(nums[i]);
                counts.push_back(1);
            }
        }

        for(int i = 0; i < counts.size(); i++){

            cout << counts[i] << ' ';
        }
        cout <<endl;
        return 0;
    }

    int find(int key){

        for(int i = 0; i < list.size(); i++){

            if(list[i] == key){

                return i;
            }
        }
        return -1;
    }
};

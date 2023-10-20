class Solution {
public:
    string maximumTime(string time) {
        vector<int> qs;
        for(int i = 0; i < time.size(); i++){

            if (time[i] == '?'){

                //cout << i <<endl;
                qs.push_back(i);
            }
        }

        for(int i = 0; i < qs.size(); i++){

            int cur = qs[i];
            if(cur == 0){

                time[cur] = '2';
            }
            if(cur == 1){

                if(time[0] == '2'){

                    time[cur] = '3';
                }
                else{
                    time[cur] = '9';
                }
            }
            if(cur == 3){

                time[cur] = '5';
            }
            if(cur == 4){

                time[cur] = '9';
            }

        }

        if(time[0] == '2' && time[1]- '0' > '3'-'0'){

            time[0] = '1';
        }

        return time;
    }
};
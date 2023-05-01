//problem : https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/

class Solution {
public:
    double average(vector<int>& salary) {
        
        int max = 0;
        int min = 0;

        double ans = 0;
        for(int i = 0; i < salary.size(); i++){

            ans += salary[i];
            if(salary[max] < salary[i]){

                max = i;
            }

            if(salary[min] > salary[i]){

                min = i;
            }
        }

        ans = ans - salary[max] - salary[min];
        ans = ans/(salary.size()-2);
        return ans;
    }
};

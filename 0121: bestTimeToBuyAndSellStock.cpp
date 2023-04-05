class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int min = prices[0];
        int best = 0;
        for(int i = 1; i < prices.size(); i++){

            int current = prices[i] - min;
            if( current > best ){

                best = current;
            }

            if(min > prices[i]){

                min = prices[i];
            }
        }
        return best;
    }
};

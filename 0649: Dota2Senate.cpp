// problem : https://leetcode.com/problems/dota2-senate/description/

class Solution {
public:
    string predictPartyVictory(string senate) {

        queue<int> r;
        queue<int> d;
        int n = senate.length();   
        for(int i = 0; i < senate.size(); i++){

            if(senate[i] == 'R'){

                r.push(i);
            }
            else{

                d.push(i);
            }
        }


        while(!r.empty() && !d.empty()){

            int rid = r.front(), did = d.front();
            r.pop(), d.pop();
            if(rid < did) r.push(rid + n);
            else d.push(did + n);            
        }

        return (r.size() > d.size())? "Radiant" : "Dire";

    }
};

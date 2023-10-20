class Solution {
public:
    int binaryGap(int n) {
        vector<int>index;
        int i=0;
        int ans=0;
        while(n!=0)
        {
            if(n%2==1)
            {
                index.push_back(i);
            }
            i++;
            n=n/2;
        }
        for(i=1; i<index.size(); i++)
        {
            ans=max(ans, abs(index[i]-index[i-1]));
        }
        return ans;
    }
};
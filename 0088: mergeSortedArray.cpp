class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        vector<int> ans;
        int j = 0;
        int i = 0;
        while(i < n && j < m){

            if(nums1[j] > nums2[i]){

                cout << nums2[i] <<' ';
                ans.push_back(nums2[i]);
                i++;
            }
            else if(nums1[j] < nums2[i]){

                ans.push_back(nums1[j]);
                j++;
            }
            else if(nums1[j] == nums2[i]){

                ans.push_back(nums2[i]);
                ans.push_back(nums2[i]);
                j++;
                i++;
            }
        }

        for(; i < n; i++){

            ans.push_back(nums2[i]);
        }

        for(; j < m; j++){

            ans.push_back(nums1[j]);
        }

        nums1 = ans;
    }
};

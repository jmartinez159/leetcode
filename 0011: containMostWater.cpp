//problem : https://leetcode.com/problems/container-with-most-water/description/

class Solution {
public:

    

    int maxArea(vector<int>& height) {

        int max = 0;
        int left = 0;
        int right = height.size()-1;
        while(left < right){

            int h;
            if(height[left] < height[right]){

                h = height[left];
                left++;
            }

            else{

                h = height[right];
                right--;
            }

            int a = h*(right- left+1); 
            if(a > max){

                max = a;
            }

        }

        return max;
    }
};

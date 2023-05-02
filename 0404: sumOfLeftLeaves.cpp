// problem : https://leetcode.com/problems/sum-of-left-leaves/description/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    bool isLeft;
    int ans = 0;  

    int sumOfLeftLeaves(TreeNode* root) {


        if(!root){

            return 0;
        }

        if(!root->left && !root->right){

            if(isLeft){

                ans += root->val;
            }

            return 0;
        }

        isLeft = true;
        sumOfLeftLeaves(root->left);
        isLeft = false;
        sumOfLeftLeaves(root->right);

        
        return ans;
    }

};

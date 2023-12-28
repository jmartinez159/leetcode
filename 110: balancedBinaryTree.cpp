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

    int ans;

    bool isBalanced(TreeNode* root) {
        
        ans = 0;
        height(root);
        return ans != INT_MAX;
    }

    int height(TreeNode* root){

        if(!root){

            return 0;
        }

        int left = height(root->left);
        int right = height(root->right);
        int h = left-right;
        if(h > 1 || h < -1)
            ans = INT_MAX;
        return max(left+1, right+1);
    }
};
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

    int ans = 0;

    int diameterOfBinaryTree(TreeNode* root) {

        solve(root);
        return ans;
    }

    int solve(TreeNode *root){

        if(!root){
            return -1;
        }
        
        if(!root->left && !root->right){
            return 0;
        }

        int left = solve(root->left) +1;
        int right = solve(root->right) +1;
        ans = max(ans, left+right);
        return max(left,right);
    }
};
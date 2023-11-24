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
    bool checkTree(TreeNode* root) {
        
        if(!root){
            return false;
        }

        return root->val == sums(root->left)+sums(root->right);
    }

    int sums(TreeNode* root){

        if(!root){

            return 0;
        }

        int ans = root->val + sums(root->left) + sums(root->right); 
        return ans;
    }
};
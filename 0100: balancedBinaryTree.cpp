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
    bool isBalanced(TreeNode* root) {
        
        if(root == nullptr){

            return true;
        }

        int check = height(root->left) - height(root->right);

        if(check<0){

            check*=-1;
        }

        if(check > 1){

            return false;
        }

        if(!isBalanced(root->left)){

            return false;
        }
        
        
        if(!isBalanced(root->right)){

            return false;
        }

        
        return true;

    }

    int height(TreeNode* root){

        if(root == nullptr){

            return 0;
        }

        return max(height(root->left)+1, height(root->right)+1);
    }
};

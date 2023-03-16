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
    bool hasPathSum(TreeNode* root, int targetSum) {
        
        if(root == nullptr){
        
            return false;
        }

        return valid(root, targetSum);
    }

    bool valid(TreeNode* root, int sum){

        if(root == nullptr){

            return false;
        }

        if(root->left == nullptr && root->right == nullptr){

            if(sum == root->val){

                return true;
            }

            return false;
        }
        sum -= root->val;

        return valid(root->left, sum) || valid(root->right, sum);

        
    }
};

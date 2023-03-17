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

    int minDepth(TreeNode* root) {

        if(root == nullptr){

            return 0;
        }

        int ans = -1;

        helper(root, 1, ans);

        return ans;        
    }

    void helper(TreeNode* root, int level, int& ans){

        if(root==nullptr){

            return;
        }

        if(root->left == nullptr && root->right == nullptr){

            if(ans == -1 || level < ans){

                ans = level;
            }
            
        }
        
        else{

            helper(root->left, level+1, ans);
            helper(root->right, level+1, ans);
        }

        

    }
};

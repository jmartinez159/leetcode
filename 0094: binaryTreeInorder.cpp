//problem : https://leetcode.com/problems/binary-tree-inorder-traversal/description/

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

    vector<int> ans;

    vector<int> inorderTraversal(TreeNode* root) {
        
        check(root);        
        return ans;
    }

    void check(TreeNode* root){

        if(!root){

            return;
        }

        check(root->left);

        ans.push_back(root->val);

        check(root->right);

        return;

    }

};

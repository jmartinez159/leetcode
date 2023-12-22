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

    vector<vector<int>> ans;

    vector<vector<int>> levelOrder(TreeNode* root) {
        
        traverse(root, 1);
        return ans;
    }

    void traverse(TreeNode *root, int level){

        if(!root){

            return;
        }

        if(level > ans.size()){
            ans.push_back(vector<int>());
        }

        ans[level-1].push_back(root->val);
        traverse(root->left, level+1);
        traverse(root->right, level+1);
    }
};
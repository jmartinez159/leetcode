//problem : https://leetcode.com/problems/range-sum-of-bst/description/

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
    int rangeSumBST(TreeNode* root, int low, int high) {
        
        int ans = 0;

        if(!root){

            return 0;
        }

        if(root->val >= low && root->val <= high){

            ans += root->val;
        }

        if(!root->left && !root->right){

            return ans;
        }

        ans += rangeSumBST(root->left, low, high);
        ans += rangeSumBST(root->right, low, high);

        return ans;

    }
};

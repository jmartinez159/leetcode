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
    vector<int> rightSideView(TreeNode* root) {
        
        if(!root){

            return {};
        }

        queue<TreeNode*> q;
        q.push(root);
        vector<int> ans;

        while(!q.empty()){

            int count = q.size();
            for(int i = count; i > 0; i--){

                TreeNode* cur = q.front();
                q.pop();

                if(i == count){
                    ans.push_back(cur->val);
                }

                if(cur->right){
                    q.push(cur->right);
                }

                if(cur->left){
                    q.push(cur->left);
                }
            }
        }

        return ans;
    }
};
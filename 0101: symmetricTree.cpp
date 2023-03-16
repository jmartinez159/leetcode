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
    bool isSymmetric(TreeNode* root) {

        return valid2(root, root);
    }

    bool valid(TreeNode* right, TreeNode* left){

        if(right == nullptr && left == nullptr){

            return true;
        }

        if(right == nullptr || left == nullptr || right->val != left->val){

            return false;
        }

        return valid(right->right, left->left) && valid(right->left, left->right); 

    }

    //fancy solution (mimicking truth table)
    bool valid2(TreeNode* right, TreeNode* left){

        return (!right && !left) || 
                (  
                   
                   left && right 
                && left->val == right->val 
                && valid2(right->right, left->left) 
                && valid2(right->left, left->right) 

                );   
                //left && right if either null the we get a false
    }
};

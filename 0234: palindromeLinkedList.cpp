/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        
        stack<int> check;
        auto current = head;
        while(current){

            check.push(current->val);
            current = current->next;
        }

        current = head;
        while(!check.empty()){

            if(check.top() != current->val){

                return false;
            }
            //cout << check.top() << ' ' << current->val <<endl;
            check.pop();
            current = current->next;
        }

        return true;
    }
};

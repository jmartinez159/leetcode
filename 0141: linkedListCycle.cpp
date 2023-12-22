/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        set<ListNode*> check;
        ListNode* current = head;
        while(current != nullptr){

            if(check.count(current)){

                return true;
            }

            check.insert(current);
            current = current->next;
        }

        return false;
    }
};
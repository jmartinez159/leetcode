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
    ListNode* removeElements(ListNode* head, int val) {
        
        auto dummyhead = new ListNode(0, head);
        auto prev = dummyhead;
        auto current = prev->next;
        
        while(current){
            if(current->val == val){

                prev->next = current->next;
            }

            else{

                prev = current;
            }

            current = current->next;
            
        }

        return dummyhead->next;
    }
};

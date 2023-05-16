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
    ListNode* swapPairs(ListNode* head) {

        if(!head){

            return head;
        }

        if(!head->next){

            return head;
        }
        
        ListNode* n = swapPairs(head->next->next);
        ListNode* ans = head->next;
        ans->next = head;
        ans->next->next = n;
        return ans;
    }
};

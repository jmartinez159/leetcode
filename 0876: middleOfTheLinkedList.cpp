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
    ListNode* middleNode(ListNode* head) {
        int count = 0;
        auto curr = head;
        while(curr){

            count++;
            curr = curr->next;
        }
        
        count /= 2;
        for(int i = 0; i < count; i++){

            head = head->next;
        }
        
        return head;
    }
};
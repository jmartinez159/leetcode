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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
        map<int, int> freqMap;
        for(int i = 0; i<lists.size(); i++){

            ListNode* current = lists[i];
            while(current != nullptr){

                freqMap[current->val]++;
                current = current->next;
            }
        }

        ListNode* ans = new ListNode();
        ListNode* cur = ans;
        for(auto it : freqMap){

            for(int i = 0; i < it.second; i++){

                cur->next = new ListNode(it.first);
                cur = cur->next;
            }
        }

        return ans->next;
    }
};
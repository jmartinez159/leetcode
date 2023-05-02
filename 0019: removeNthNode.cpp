// problem : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        stack<ListNode*> line;
        stack<ListNode*> order;
        ListNode *ans = new ListNode();

        auto cur = head;
        while(cur){

            line.push(cur);
            cur = cur->next;
        }

        auto cans = ans;
        int i = 1;
        while(!line.empty()){

            if(i != n){

                order.push(line.top());
            }
            line.pop();
            i++;
        }

        while(!order.empty()){

            // cout << order.top()->val <<endl;
            cans->next = order.top();
            cans = cans->next;
            order.pop();
        }

        cans->next = nullptr; 

        // cout << line.size() <<endl;
        return ans->next;
    }
};

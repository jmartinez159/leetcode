//problem : https://leetcode.com/problems/intersection-of-two-linked-lists/description/

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        
        ListNode *cur1 = headA;
        ListNode *cur2 = headB;

        map<ListNode*, int> map;

        while(cur1){

            cout << cur1 << ' ';
            map[cur1] = cur1->val;
            cur1 = cur1->next;
        }
        cout <<endl;

        while(cur2){

            cout << cur2 << ' ';
            if(map[cur2] != 0){

                return cur2;
            }
            cur2 = cur2->next;
        }

        return nullptr;
    }
};

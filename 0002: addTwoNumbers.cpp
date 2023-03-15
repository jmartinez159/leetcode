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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode *ans = new ListNode();
        ListNode * tail = ans;
        int curr;
        int carry = 0;
        while(l1 != nullptr && l2 != nullptr){

            curr = carry +l1->val +l2->val; //adding values
            carry = 0;
            if(curr >= 10){ //checking if our value is greater than 10 for carry val

                curr -= 10;
                carry = 1;
            }
            
            //adding new sum to our linked list
            tail->next = new ListNode(curr);
          
            //incrementing nodes to next node
            tail = tail->next;
            l1 = l1->next;
            l2 = l2->next;
        }

        //adding leftover nodes
        while(l1 != nullptr){

            curr = carry +l1->val;
            carry = 0;
            if(curr >= 10){

                curr -= 10;
                carry = 1;
            }

            tail->next = new ListNode(curr);
            tail = tail->next;
            l1 = l1->next;
        }

        //adding leftover nodes
        while(l2 != nullptr){

            curr = carry +l2->val;
            carry = 0;
            if(curr >= 10){

                curr -= 10;
                carry = 1;
            }

            tail->next = new ListNode(curr);
            tail = tail->next;
            l2 = l2->next;
        }
      
        //checking for one last carry value
        if(carry == 1){

            tail->next = new ListNode(1);
        }

        return ans->next;
    }
};

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    
    int size = 0;
    struct ListNode* cur = head;
    while(cur != NULL){

        size++;
        cur = cur->next;
    }

    cur = head;
    int* arr = (int*)malloc(size*sizeof(int));
    int i = 0;
    while(cur != NULL){

        arr[i] = cur->val;
        i++;
        cur = cur->next;
    }

    cur = head;
    for(int i = 0; i < size; i++){

        cur->val = arr[size-1-i];
        cur = cur->next;
    }
    
    return head;
}
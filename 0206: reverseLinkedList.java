/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        
        ListNode cur = head;
        Stack<ListNode> stack = new Stack<ListNode>();
        while(cur != null){

            stack.push(cur);
            cur = cur.next;
        }

        ListNode res = new ListNode();
        cur = res;

        while(!stack.empty()){

            cur.next = stack.pop();
            cur = cur.next;
        }

        if(cur != null){

            cur.next = null;
        }
        return res.next;
    }
}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode DoubleIt(ListNode head) {
        
        List<int> num = new List<int>();
        ListNode curr = head;
        while(curr != null){

            num.Add(curr.val);
            curr = curr.next;
        }

        Stack<int> st = new Stack<int>();
        int carry = 0;
        for(int i = 0; i < num.Count; i++){

            int temp = (2*num[num.Count-1-i])+carry;
            carry = temp/10;
            temp = temp%10;
            st.Push(temp);
        }

        if(carry == 1){

            st.Push(carry);
        }

        ListNode res = new ListNode(0);
        curr = res;

        while(st.Count > 0){

            curr.next = new ListNode(st.Pop());
            curr = curr.next;
        }

        return res.next;
    }
}
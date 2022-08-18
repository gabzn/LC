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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if(list1 == null && list2 == null) return null;
        if(list1 == null) return list2;
        if(list2 == null) return list1;
        
        // Find the first smallest node between both lists.
        ListNode newHead;
        if(list1.val <= list2.val) {
            newHead = new ListNode(list1.val);
            list1 = list1.next;
        } else {
            newHead = new ListNode(list2.val);
            list2 = list2.next;
        }
        
        // Use ptr to connect all the remaining nodes.
        // Loop through both lists and compare both vals
        ListNode ptr = newHead;
        while(list1 != null && list2 != null) {
            if(list1.val <= list2.val) {
                ptr.next = new ListNode(list1.val);
                list1 = list1.next;
            } else {
                ptr.next = new ListNode(list2.val);
                list2 = list2.next;
            }
            ptr = ptr.next;
        }
        
        if(list1 == null) {
            ptr.next = list2;
        } else {
            ptr.next = list1;
        }
        
        return newHead;
    }
}

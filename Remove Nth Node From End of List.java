Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

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
class Solution 
{
    public ListNode removeNthFromEnd(ListNode head, int n) 
    {      
        // Get the size of the linked list.
        int size = getSize(head);
        
        // Two helper nodes point to the head node.
        // mover finds the target node and stops at it's previous node.
        ListNode temp = new ListNode();
        temp.next = head;
        ListNode mover = temp;
           
        for(int i=0;i<(size-n);i++)
        {
            mover = mover.next;
        }
        
        // remove the target node.
        mover.next = mover.next.next;
        return temp.next;
    }
    
    public int getSize(ListNode head)
    {
        ListNode temp = head;
        
        int size = 0;
        while(temp != null)
        {
            temp = temp.next;
            size++;
        }
        
        return size;
    }
}

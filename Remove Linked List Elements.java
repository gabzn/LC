Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]


class Solution 
{
    public ListNode removeElements(ListNode head, int val) 
    {
        // Edge case where the list is empty.
        if(head == null) return head;
        
        // Three pointers but only prev and runner will be moving.
        ListNode prev = new ListNode(-1, head);
        ListNode toReturn = prev;
        ListNode runner = head;
        
        // Go through the list.
        while(runner != null)
        {
            // If the current node has the target value, remove it by changing the prev.next to current node next.
            // Else move the prev pointer.
            // Prev pointer needs to move when it's next node doesn't have the value of val.
            if(runner.val == val)    prev.next = runner.next;
            else                     prev = prev.next;

            runner = runner.next;
        }
    
        return toReturn.next;
    }
}

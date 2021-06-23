Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

public class Solution 
{
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) 
    {
        if(headA == null || headB == null) return null;

        // Use a helper function to get the size of each list.
        int sizeA = getSize(headA);
        int sizeB = getSize(headB);
        
        ListNode a = headA;
        ListNode b = headB;
        
        // If both lists have the same size, this question will be very straightforward.
        // Same size : check each node from each list to see if they point to the same location. Return the node if they do.
        // Different size : shorten the longer list until they have the same size. Then repeat the same size procedure.
        while(sizeA > sizeB)
        {
            a = a.next;
            sizeA--;
        }
        
        while(sizeB > sizeA)
        {
            b = b.next;
            sizeB--;
        }
        
        while(a != null)
        {
            if(a == b) return a;
            
            a = a.next;
            b = b.next;
        }
        
        return null;
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

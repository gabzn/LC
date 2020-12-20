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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) 
    {
        if(l1==null && l2==null) return null;
        if(l1==null) return l2;
        if(l2==null) return l1;
            
        ListNode toReturn;
        
        //Find the first smallest value in the given lists.
        if(l1.val<=l2.val)
        {
            toReturn = new ListNode(l1.val);
            l1 = l1.next;
        }else
        {
            toReturn = new ListNode(l2.val);
            l2 = l2.next;
        }
        
        //Initialize a pointer. Temp will link all other nodes in order.
        ListNode temp = toReturn;
        
        //As long as neither of them is null, keep adding the smaller one to toReturn.
        //After adding a node to toReturn, remove that node from the list.
        while(l1 != null && l2 != null)
        {
            if(l1.val<=l2.val)
            {
                temp.next = new ListNode(l1.val);
                l1 = l1.next;
            }
            else
            {
                temp.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            temp = temp.next;
        }
        
        while(l1 != null)
        {
            temp.next = new ListNode(l1.val);
            temp = temp.next;
            l1 = l1.next;
        }
        
        while(l2 != null)
        {
            temp.next = new ListNode(l2.val);
            temp = temp.next;
            l2 = l2.next;
        }
            
        return toReturn;  
    }
}

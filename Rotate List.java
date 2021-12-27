Given the head of a linked list, rotate the list to the right by k places.
  
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]

class Solution 
{
    public ListNode rotateRight(ListNode head, int k) {
        if(k == 0 || head == null) return head;
        
        int length = getLength(head);
        if(length == 1 || (k % length) == 0) return head;
        
        // Example 2 shows that if k > length, the result is just the same as rotating the list k % length times.
        k = k % length;
        
        // tailPtr will point to the end of the list.
        // newHead will point to the k-th element from the back of the list.
        // prevNewHead will point to the previous element of new head.
        ListNode tailPtr = head;
        ListNode newHead = head;
        ListNode prevNewHead = new ListNode();
        prevNewHead.next = newHead;
        
        // The number of moves to find the new head node.
        int moves = length - k;
        
        while(tailPtr.next != null) {
            
            if(moves > 0) {
                newHead = newHead.next;
                prevNewHead = prevNewHead.next;
            }
            
            moves--;
            tailPtr = tailPtr.next;
        }
        
        prevNewHead.next = null;
        tailPtr.next = head;
        head = newHead;
        
        return head;
    }
    
    public int getLength(ListNode head) {
        ListNode ptr = head;
        int length = 0;
        while(ptr != null) {
            length++;
            ptr = ptr.next;
        }
        return length;
    }
}

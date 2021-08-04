Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.
  
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [1,2,3,4,5,6]
Output: [1,3,5,2,4,6]

class Solution 
{
    public ListNode oddEvenList(ListNode head) 
    {
        // Edge cases. The second check is not necessary, but it helped me to solve the problem in the first place.
        if(head == null) return null;
        // if(head.next == null) return head; 
        
        // oddIndex and evenIndex will move through the list. 
        // evenHead stays at the second node.
        ListNode oddIndex = head;
        ListNode evenIndex = head.next;
        ListNode evenHead = head.next;
        
       // 2 scenarios. The length of the list is either odd or even.
       // evenIndex != null handles when the length is odd.
       // oddIndex.next.next != null handles when the length is even.
        while(evenIndex != null && oddIndex.next.next != null)
        {
            oddIndex.next = evenIndex.next;
            oddIndex = oddIndex.next;
            evenIndex.next = oddIndex.next;
            evenIndex = evenIndex.next;
        }
        
        oddIndex.next = evenHead;
        return head;
    }
}

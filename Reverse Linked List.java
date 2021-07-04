Given the head of a singly linked list, reverse the list, and return the reversed list.
  
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

class Solution 
{
    public ListNode reverseList(ListNode head) 
    {      
        // Edge case where the list is empty.
        if(head == null) return null;
        
        // Two helper pointers move at the same time.
        ListNode prev = null;
        ListNode nextNode = head.next;
        
        // While the nextNode has not reached the end of the list.   
        // Reverse head.next. Have it pointing to it's previous node.  ----------> Line 22.
        // Advance all three pointers.                                 ----------> Line 23 24 25.
        while(nextNode != null)
        {
            head.next = prev;
            prev = head;
            head = nextNode;
            nextNode = nextNode.next;
        }
        
        // At the very last iteration of the loop, head would be at the last node in the list.
        // Because the condition is false, line 22 would not get executed. 
        head.next = prev;
        return head;
    }
}

Before 1st iteration:            null        1     ->       2       ->      3      ->     4  
                                 prev       head         nextNode


1st iteration:                   null   <-     1            2       ->      3      ->     4   
                                  prev       head        nextNode  

                                 null   <-     1            2       ->      3      ->     4   
                                          prev,head        nextNode  

                                 null   <-     1            2       ->      3      ->     4    
                                             prev        head,nextNode  
                                            
                                 null   <-     1            2       ->      3      ->     4    
                                             prev        head           nextNode  


2nd iteration:                    null   <-     1      <-      2            3      ->     4    
                                             prev           head          nextNode  
                                             
                                  null   <-     1      <-      2            3      ->     4    
                                                           prev,head      nextNode  
                                                           
                                  null   <-     1      <-      2            3      ->     4    
                                                              prev      head,nextNode 
                                                              
                                  null   <-     1      <-      2            3      ->     4    
                                                              prev      head          nextNode  


                                             
3rd iteration:                    null   <-     1      <-      2      <-      3           4    
                                                              prev          head       nextNode  
              
                                  null   <-     1      <-      2      <-      3           4    
                                                                          prev, head   nextNode  
                                                                          
                                  null   <-     1      <-      2      <-      3           4    
                                                                            prev      head,nextNode  

                                  null   <-     1      <-      2      <-      3           4           null
                                                                            prev         head       nextNode
    
    
 Condition failed                 null   <-     1      <-      2      <-      3     <-    4
                                                                            prev         head        
  

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

 // 1---2---3---4---5---6--NULL                     parentNext = 4---5---6--NULL   
 //         |
 //         7---8---9---10--NULL                    parentNext = 9---10--NULL     
 //             |
 //             11--12--NULL

class Solution 
{
    public Node flattenNodes(Node head)
    {
        Node ptr = head;   
        Node end = head;
        
        while(ptr != null)
        {
            // Do something when the node has a child. Otherwise, move the pointer.
            if(ptr.child != null)
            {
                // If the current node has a child, store it's next first.
                Node parentNext = ptr.next;
                Node flattenedEnd = flattenNodes(ptr.child);
                
                // Assuming all work out, flattenNodes returns the end of the flattened list.
                // Connect both the end and the parentNext.
                flattenedEnd.next = parentNext;
                if(parentNext != null) parentNext.prev = flattenedEnd;
                
                // Change pointers between child and parent. Since the child has become it's parent next,
                // Null out parent.child once the connection between them is done.
                ptr.next = ptr.child;
                ptr.child.prev = ptr;
                ptr.child = null;
            }
            else ptr = ptr.next;
            
            // Very crucial sinendce I want the end of the flattened list to be returned. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if(ptr != null) end = ptr;
        }
        return end;
    }
    
    public Node flatten(Node head) 
    {
        if(head == null) return null;
        flattenNodes(head);
        return head;
    }    
}

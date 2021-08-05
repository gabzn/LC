Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2,3,2,1]
Output: true

Input: head = [1,2]
Output: false

------------------------------------------------------------------------------------------------------------------------------
                                                                Stack solution

class Solution 
{
    public boolean isPalindrome(ListNode head) 
    {
        if(head.next == null) return true;
        
        int length = getLength(head);
        
        // Using a stack to store the left-half of the data.
        // middleIndex indicates where the left-half ends.
        
        int middleIndex = (length/2) - 1;
        Stack<Integer> stack = new Stack<>();
        int stackSize = 0;
        
        // Push the first val into the stack first.
        
        ListNode runner = head;
        stack.push(runner.val);

        while(stackSize != middleIndex)
        {
            runner = runner.next;
            stack.push(runner.val);
            stackSize++;
        }
        
        // If the length is even, there is no middle val. For example:  [1,2,2,1]. Runner should be at the second 2.
        // If the length is odd, there is a middle val. For example: [1,2,3,2,1]. 3 is the middle val. Runner should ignore it by doing runner.next.next.
        
        if(length%2 == 0) runner = runner.next;
        else runner = runner.next.next;
        
        while(runner != null)
        {
            if(stack.pop() != runner.val) return false;
            runner = runner.next;
        }
        return true;
    }
    
    public int getLength(ListNode head)
    {
        ListNode ptr = head;
        int length = 0;
        while(ptr != null)
        {
            ptr = ptr.next;
            length++;
        }
        return length;
    }
}

------------------------------------------------------------------------------------------------------------------------
                                                                Two-pointer solution

class Solution 
{
    public boolean isPalindrome(ListNode head) 
    {
        if(head.next == null) return true;
        
        // fast pointer will go 2 steps at a time. Whereas, slow pointer will go 1 step at a time.
        // When fast gets to the last node or null, slow will always be at the middle of the list. This is the most confusing part!!!
        
        ListNode fast = head;
        ListNode slow = head;
        
        // fast != null handles when the length of the list is even.
        // fast.next != null handles when the length of the list is odd.
        
        while(fast != null && fast.next != null)
        {
            fast = fast.next.next;
            slow = slow.next;
        }
        
        // Reverse the right half of the list starting with slow pointer.
        
        ListNode prev = null;
        
        while(slow != null)
        {
            ListNode after = slow.next;
            slow.next = prev;
            prev = slow;
            slow = after;
        }
        
        // Reset slow to the head because when the loop above finishes, slow is always null. 
        // prev will be the head of the reversed list.
        
        slow = head;
        while(prev != null)
        {
            if(prev.val != slow.val) return false;
            slow = slow.next;
            prev = prev.next;
        }
        
        return true;
    }
}

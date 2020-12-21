class Solution 
{
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) 
    {
        //'carry' indicates whether there's a carry or not.
        boolean carry = false;
        ListNode toReturn;
        
        //Get the first sum.
        int sum = l1.val + l2.val;
        int remainder;
        
        //Check if 'sum' is larger or equal to 10.
        //If it is, take only the remainder, initialize 'toReturn' and change 'carry' to true.
        //Otherwise, take the sum, initialize 'toReturn' and leave 'carry' as false.
        if(sum >= 10) 
        {
            remainder = sum % 10;
            carry = true;
            toReturn = new ListNode(remainder);
        }
        else    toReturn = new ListNode(sum);
        
        //Move both lists' pointers to the next elements.
        l1 = l1.next;
        l2 = l2.next;
        
        //New pointer pointing to the tail of toReturn.
        ListNode temp = toReturn;
        
        //Go through both lists and add sum.
        while(l1 != null && l2 != null)
        {
            if(carry) sum = l1.val + l2.val + 1;
            else      sum = l1.val + l2.val;
                
            if(sum>=10)
            {
               remainder = sum % 10;
               carry = true;
               temp.next = new ListNode(remainder);
            }
            else 
            {
               carry = false;
               temp.next = new ListNode(sum);
            }
            
            temp = temp.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        //Check the case where one list has more digits than the other.
        while(l1 != null)
        {
            if(carry) sum = l1.val + 1;
            else sum = l1.val;
            
            if(sum >= 10)
            {
                remainder = sum % 10;
                carry = true;
                temp.next = new ListNode(remainder);
            }
            else
            {
                carry = false;
                temp.next = new ListNode(sum);
            }
            l1 = l1.next;
            temp = temp.next;
        }
        
        while(l2 != null)
        {
            if(carry) sum = l2.val + 1;
            else sum = l2.val;
            
            if(sum >= 10)
            {
                remainder = sum % 10;
                carry = true;
                temp.next = new ListNode(remainder);
            }
            else
            {
                carry = false;
                temp.next = new ListNode(sum);
            }
            l2 = l2.next;
            temp = temp.next;
        }
        
        if(carry) temp.next = new ListNode(1);
        return toReturn;
    }
}

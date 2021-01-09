class Solution 
{
    public String addBinary(String a, String b) 
    {
      StringBuilder sb = new StringBuilder();
      int al = a.length() - 1;
      int bl = b.length() - 1;
      int carry = 0;
        
      while(al >= 0 && bl >= 0)
      {
          # Key thing to learn is how to convert a char to an int.
          int sum = (a.charAt(al) - '0') + (b.charAt(bl) - '0') + carry;
          
          # sum can either be 2 or 3 if this condition is true.
          if(sum >= 2)
          {
              carry = 1;
              sum = sum % 2;
              sb.insert(0,sum);
          }
          else
          {
              carry = 0;
              sb.insert(0,sum);
          }
          
          al--;
          bl--;
      }
       
       # Cases where one string is longer than the other.
       while(al >= 0)
       {
           if( (a.charAt(al) - '0') + carry == 2)
           {
               sb.insert(0,0);
               carry = 1;
           }
           else
           {
               sb.insert(0,(a.charAt(al) - '0') + carry);
               carry = 0;
           }
           al--;
       }
        
       while(bl >= 0)
       {
           if( (b.charAt(bl) - '0') + carry == 2)
           {
               sb.insert(0,0);
               carry = 1;
           }
           else
           {
               sb.insert(0,(b.charAt(bl) - '0') + carry);
               carry = 0;
           }
           bl--;
       }
       
       # Final case where the leftmost number also gives a carry, if it gives a carry, append a '1' to the very beginning of the string.
       if(carry == 1) sb.insert(0,1);
       return sb.toString();
    }
}

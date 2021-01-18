class Solution 
{
    public boolean isPalindrome(String s) 
    {
        if(s.length() == 0 || s.length() == 1) return true;
        
        s = s.toLowerCase();
        
        int i = 0;
        int j = s.length() - 1;
        
        while(i <= j)
        {
            if( !Character.isLetterOrDigit(s.charAt(i)) || !Character.isLetterOrDigit(s.charAt(j)))
            {
                if( !Character.isLetterOrDigit(s.charAt(i)) && !Character.isLetterOrDigit(s.charAt(j)))
                {
                    i++;
                    j--;
                    continue;
                }
                else if ( !Character.isLetterOrDigit(s.charAt(i)) )
                {
                    i++;
                    continue;
                }
                else
                {
                    j--;
                    continue;
                }
            }
            
            if(s.charAt(i) != s.charAt(j)) return false;
            i++;
            j--;
        }
        
        return true;
    }
}

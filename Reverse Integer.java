class Solution 
{
    public int reverse(int x) 
    {
        int toReturn = 0;
        
        while(x != 0)
        {
            if(toReturn < Integer.MIN_VALUE/10 || toReturn > Integer.MAX_VALUE/10) return 0;
            toReturn = toReturn*10 + x%10;
            x = x/10;
        }
        
        return toReturn;
    }
}

//Use % when dealing with reversing an integer.

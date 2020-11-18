class Solution 
{
    public int reverse(int x) 
    {
        int toReturn = 0;
        
        while(x != 0)
        {
            if(toReturn < Integer.MIN_VALUE/10 || toReturn > Integer.MAX_VALUE/10) return 0;  //Every iteration 'toReturn' is going to multiply by 10.
                                                                         //We want to make sure that 'toReturn' doesn't get beyong the scope of Integer when it's multiply by 10 next time.
                                                                         //We can check that by comparing the MIN and MAX values of Integer dividing by 10.                 
            toReturn = toReturn*10 + x%10;
            x = x/10;
        }
        
        return toReturn;
    }
}
//Use % when dealing with reversing an integer.

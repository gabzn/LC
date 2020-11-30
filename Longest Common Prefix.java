class Solution 
{
    public String longestCommonPrefix(String[] strs) 
    {
        if(strs.length == 0) return "";

        int totalString = strs.length;
        
        //Assuming the first string is the most common prefix.
        String prefix = strs[0]; 

        //'i' starts at 1 instead of 0 because there's no need to compare the first string in the array.
        for(int i=1;i<totalString;i++) 
        {
            //'toCompare' will be assigned every string in each iteration.
            String toCompare = strs[i]; 
            
            //While 'prefix' is not equal to current 'toCompare', cut the last character of 'prefix' until the condition is met.
            //As long as 'prefix' is not equal to 'toCompare', take out the last character of prefix until they are equal.
            while(!prefix.equals(toCompare) && toCompare.indexOf(prefix)!= 0)  
            {
                prefix = prefix.substring(0,prefix.length()-1);
            }
        }
        return prefix;
    }
}
// ["flower","flow","flight"]
//First off, assume the first string in the array is the longest common prefix. ------------> (In this case, flower)
//Then, compare every other strings in the array to shorten/modify (if necessary) the prefix.

//String a.indexOf(String b) method     ----->     (If string b is longer than string a, then it will always return 0 because there's no way b can go into a.) 
//flow.indexOf(flower) will return -1 because 'flower' cannot go into 'flow'.
//flower.indexOf(flow) will return 0 because 'flow' can go into 'flower', starting with index 0;                

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "dvdfadbf"
Output: 4
Explanation: The answer is "vdfa", with the length of 4.


class Solution 
{
    public int lengthOfLongestSubstring(String s) 
    {
        int lp = 0;
        int rp = 0;
        int max = 0;
        Set<Character> set = new HashSet<>();            ------------------->  Without repeating means 'Uniqueness'.
        
        while(rp < s.length())
        {
            if( !( set.contains(s.charAt(rp)) ) )        ------------------->  If the set does not contain the current character, add it to the set and move the pointer.
            {
                set.add(s.charAt(rp));
                rp++;
                
                if(set.size() > max) max = set.size();    ----------------> Update the max length if necessary.
            }
            else      -----------------------> If the set does contain the current character, remove every single character comes before and including the repeating character. 
            {
                set.remove(s.charAt(lp));
                lp++;
            }
        }
        return max;
    }
}

//----------------------------------------------------------------------------------------------------------------------
class Solution 
{
    public int lengthOfLongestSubstring(String s) 
    {
          int cur = 0;
          int max = 0;
          StringBuilder sb = new StringBuilder();       ------------> Another solution using StringBuilder.

          for(int i=0;i<s.length();i++)    ----------------> Go through the input string. If the StringBuilder contains the current character, delete every character comes before and including the repeating character.
          {
              if(sb.toString().contains(s.charAt(i) + ""))
              {
                 if(cur > max) max = cur;
                  
                  int occur_index = sb.lastIndexOf(s.charAt(i) + "");
                  sb.delete(0,occur_index + 1);
                  
                  cur = cur - (occur_index + 1);
              }
                  sb.append(s.charAt(i));                      ---------------------> No matter what we'll append the current character to the StringBuilder.
                  cur++;
          }
        
        if(cur > max) max = cur;
        return max;
    }
}

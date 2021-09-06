Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false


class Solution 
{
    public boolean isAnagram(String s, String t) 
    {
        if(s.length() != t.length()) return false;
        
        // The key is the letter from string s. 
        // The value is the number of occurrences of a specific letter.
        Map<Character, Integer> charMap = new HashMap<>();
        
        // Go through string s and put every character and its occurrences into the map.
        for(char i : s.toCharArray())
        {
            if(charMap.containsKey(i))
            {
                int occurrences = charMap.get(i);
                charMap.put(i, ++occurrences);
            }
            else charMap.put(i, 1);
        }
        
        // Go through the second string and check if every character of it is in the map.
        // Also decrease the occurrences of each character.
        for(char i : t.toCharArray())
        {
            if(charMap.get(i) == null || charMap.get(i) <= 0) return false;
            else
            {
                int occurrences = charMap.get(i);
                charMap.put(i, --occurrences);
            }
        }
        return true;
    }
}

----------------------------------------------------------------------------------------------------

class Solution 
{
    public boolean isAnagram(String s, String t) 
    {
        if(s.length() != t.length()) return false;
        
        // 26 letters in English alphabet.
        int[] charCount = new int[26];
        
        // Go through both strings.
        for(int i=0;i<s.length();i++)
        {
            // Key thing is know how to convert a char into int by subtracting 'a' 
            charCount[ s.charAt(i) - 'a' ]++;
            charCount[ t.charAt(i) - 'a' ]--;
        }
        
        for(int i : charCount)
        {
            if(i != 0) return false;
        }
        
        return true;
    }
}

Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
  
  
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
  
class Solution {
    public int titleToNumber(String columnTitle) {
        int answer = 0;
        int length = columnTitle.length();
        
        for(int currentCharIndex=0; currentCharIndex<length; currentCharIndex++) {
            // int charValue = columnTitle.charAt(currentCharIndex) - 64;
            int charValue = columnTitle.charAt(currentCharIndex) - 'A' + 1;
            int power = length - currentCharIndex - 1;
            
            charValue = (int) Math.pow(26, power) * charValue;
            answer += charValue;
        }
        
        return answer;
    }
}

// The corresponding value for the current letter =  letterInNum * 26^power 
    
    //       Two ways to get the letterInNum AKA conversion
    //       1: letterNum = letter - 64  
    //       2: letterNum = letter - 'A' + 1

    //       power = length - currentIndex - 1


// A A A A    l = 4
// 0 1 2 3    index
// 3 2 1 0    corresponding power
// l - index - 1

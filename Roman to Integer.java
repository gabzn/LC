class Solution 
{
    public int romanToInt(String s) 
    {
      Map<Character,Integer> map = new HashMap<>();
      map.put('I',1);
      map.put('V',5);
      map.put('X',10);
      map.put('L',50);
      map.put('C',100);
      map.put('D',500);
      map.put('M',1000);
        
      int total = 0;

      for(int i=0;i<s.length();i++) {
            int current = map.get(s.charAt(i));
            
            if(i+1 < s.length()) {
                int next = map.get(s.charAt(i+1));
                
                if(next > current) {
                    current = next - current;
                    i++;
                }   
            }
          
          total += current;
      }
        
        return total;
    }
}
//Go through the string from left to right. Compare each char with the char on the right.
//If the current char is less than the next char, consider they are together and add their difference into total. Add i by an additional 1 because they are together.
//If the current char is greater than the next char, add only the current char into total. 

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
  
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
  
  
class Solution {
    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
                
        int[] digits = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        while(num != 0) {
            
            for(int i=0;i<digits.length;i++){
                
                if(num >= digits[i]) {
                    String value = romans[i];
                    sb.append(value);
                    num = num - digits[i];
                    break;
                }
                
            }
        }
        
        return sb.toString();
    }
}


class Solution {
    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
                
        int[] digits = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        for(int i=0;i<digits.length;i++){
            if( num / digits[i] != 0 ) {
                int repeatTimes = num / digits[i];
                String value = romans[i];
                
                for(int j=0;j<repeatTimes;j++) {
                    sb.append(value);   
                }
                
                num = num % digits[i];
            }
        }
        
        return sb.toString();
    }
}

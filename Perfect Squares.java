https://leetcode.com/problems/perfect-squares/

class Solution {
    public int numSquares(int n) {
        int bound = (int) Math.floor(Math.sqrt(n));
        int dp[] = new int[n+1];
        Arrays.fill(dp, n);
        
        for(int i=1; i<dp.length; i++) {
            for(int j=1; j<bound+1; j++) {
                int square = j * j;
                
                if (i-square == 0)  dp[i] = 1;
                
                if (i-square > 0) {
                    if (dp[i] > 1 + dp[i-square]) dp[i] = 1 + dp[i-square];
                }
                
                if (i - square < 0) break;
            }
        }       
        return dp[n];
    }
}

def transformation(text, t):
    MOD = 10 ** 9 + 7
    
    dp = [0] * 26
    for char in text:
        idx = ord(char) - ord('a')
        dp[idx] += 1
    
    for _ in range(t):
        next_dp = [0] * 26

        for i in range(25):
            # (dp[a] -> next_dp[b]) until (dp[y] -> next_dp[z])
            next_dp[i + 1] += dp[i] % MOD

        # dp[z] -> next_dp[a] and next_dp[b]
        next_dp[0] += dp[-1] % MOD
        next_dp[1] += dp[-1] % MOD

        dp = next_dp

    answer = 0

    for count in dp:
        answer += count
        answer %= MOD
    
    return answer % MOD

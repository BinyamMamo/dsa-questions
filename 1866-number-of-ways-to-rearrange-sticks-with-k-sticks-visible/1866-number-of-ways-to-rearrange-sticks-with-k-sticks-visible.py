class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j] = ways with i sticks and j visible
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            # j cannot exceed i
            for j in range(1, min(i, k) + 1):
                dp[i][j] = (dp[i-1][j-1] + (i-1) * dp[i-1][j]) % MOD
        
        return dp[n][k]

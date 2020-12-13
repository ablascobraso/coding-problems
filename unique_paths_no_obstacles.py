class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        
        dp = [[0 for i in range(cols)] for i in range(rows)]
        
        for row in range(rows):
            dp[row][0] = 1
            
        for col in range(cols):
            dp[0][col] = 1
            
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[rows-1][cols-1]

def solution(land):
    answer = 0
    
    dp = land
    
    for i in range(1,len(land)):
        
        for j in range(4):
            max_value = []
            for k in range(4):
                
                if j == k:
                    continue
                max_value.append(dp[i-1][k])
            dp[i][j] = dp[i][j] + max(max_value)
    
    return max(dp[-1])
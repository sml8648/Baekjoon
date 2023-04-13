def solution(alp, cop, problems):

    max_alp = 0
    max_cop = 0
    time = 0
    for a, b, c, d, e in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, b)
        time += e
    # 목표 알고력
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0


    dp[alp][cop] = 0
    for i in range(alp,max_alp+1):

        for j in range(cop,max_cop+1):

            if (j+1) <= max_cop:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j+1])

            if (i+1) <= max_alp:
                dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j])

            # alp가 i
            for p_al, p_co, r_al, r_co, cost in problems:
                if i >= p_al and j >= p_co:
                    new_p_al = i + r_al
                    new_p_co = j + r_co

                    if new_p_al > max_alp: new_p_al = max_alp
                    if new_p_co > max_cop: new_p_co = max_cop

                    dp[new_p_al][new_p_co] = min(dp[i][j] + cost, dp[new_p_al][new_p_co])

    return dp[-1][-1]
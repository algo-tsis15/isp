def solution(n):
    dp = [0] * 60001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 60001):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 1000000007
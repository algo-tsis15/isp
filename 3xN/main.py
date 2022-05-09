def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    dp[0] = 1
    sub = 0
    for i in range(2, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + sub * 2
        sub += dp[i - 2]

    answer = dp[n] % 1000000007

    return answer
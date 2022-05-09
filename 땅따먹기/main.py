import copy


def solution(land):
    dp = copy.deepcopy(land)

    for i in range(1, len(land)):
        for j in range(4):
            for t in range(4):
                # 열이 같다면 스킵
                if j == t:
                    continue
                if dp[i - 1][t] + land[i][j] > dp[i][j]:
                    dp[i][j] = dp[i - 1][t] + land[i][j]
    return max(dp[len(land) - 1])
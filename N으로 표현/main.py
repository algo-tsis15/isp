def solution(N, number):
    answer = -1

    dp = []
    for i in range(1, 9):
        all_case = set()
        now_number = int(str(N) * i)
        all_case.add(now_number)
        for j in range(0, i - 1):
            for a in dp[j]:
                for b in dp[-j - 1]:
                    all_case.add(a + b)
                    all_case.add(a - b)
                    all_case.add(a * b)
                    if b != 0:
                        all_case.add(a // b)

        if number in all_case:
            answer = i
            break
        dp.append(all_case)

    return answer
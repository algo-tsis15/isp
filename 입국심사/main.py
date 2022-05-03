def solution(n, times):
    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in times:
            tmp += mid // i

        if tmp >= n:
            end = mid - 1
        else:
            start = mid + 1

    answer = start

    return answer
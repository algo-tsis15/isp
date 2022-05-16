import heapq

def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)

    for i in range(0, n):
        m = heapq.heappop(works)
        if m >= 0:
            heapq.heappush(works, m)
            break
        m += 1
        heapq.heappush(works, m)

    answer = 0
    while len(works) > 0:
        m = heapq.heappop(works)
        answer += pow(m * -1, 2)
    return answer
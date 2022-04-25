from collections import deque


def solution(people, limit):
    people.sort(reverse=True)
    answer = 0

    q = deque(people)

    while q:
        if len(q) == 1:
            answer += 1
            break
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
        else:
            q.popleft()
        answer += 1

    return answer
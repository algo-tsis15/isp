from collections import deque


def checkWord(data_a, data_b):
    cnt = 0
    for i in range(len(data_a)):
        if data_a[i] != data_b[i]:
            cnt += 1
        if cnt == 2:
            return False
    return True


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = len(words)

    q = deque()
    q.append([begin, 0])

    while q:
        w, c = q.popleft()

        if c == len(words):
            break

        for i in words:
            # 변환 가능한지 체크
            if checkWord(w, i):
                if i == target:
                    return c + 1
                else:
                    q.append([i, c + 1])

    return answer
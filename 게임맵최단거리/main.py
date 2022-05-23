from collections import deque


def solution(maps):
    answer = -1

    len_x = len(maps)
    len_y = len(maps[0])
    x, y = 0, 0
    q = deque()
    # 위,아래, 오른쪽, 왼쪽
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    q.append([x, y, 0])
    while q:
        now_x, now_y, cnt = q.popleft()

        if now_x == len_x - 1 and now_y == len_y - 1:
            answer = cnt + 1
            break

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]

            if nx >= 0 and nx < len_x and ny >= 0 and ny < len_y:
                if maps[nx][ny] == 1:
                    q.append([nx, ny, cnt + 1])
                    maps[nx][ny] = 0

    return answer
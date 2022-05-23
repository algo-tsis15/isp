from collections import deque


def bfs(p):
    # 위1,아래1,오른쪽1,왼쪽1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    start = []

    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s])
        visited = [[0] * 5 for i in range(5)]
        distance = [[0] * 5 for i in range(5)]
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0

    return 1


def solution(places):
    answer = []
    for array in places:
        answer.append(bfs(array))

    return answer
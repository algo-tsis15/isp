from collections import deque


def solution(board):
    answer = 0
    n = len(board)

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    answer = float('inf')
    q = deque()

    q.append((0, 0, -1, 0))
    visit = {(0, 0, 0): 0, (0, 0, 1): 0, (0, 0, 2): 0, (0, 0, 3): 0}

    while q:
        x, y, d, cost = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                newcost = cost
                if d == -1:
                    newcost += 100
                elif (d - i) % 2 == 0:
                    newcost += 100
                else:
                    newcost += 600
                if nx == n - 1 and ny == n - 1:
                    answer = min(answer, newcost)
                elif visit.get((nx, ny, i)) is None or visit.get((nx, ny, i)) > newcost:
                    visit[(nx, ny, i)] = newcost
                    q.append((nx, ny, i, newcost))
    return answer
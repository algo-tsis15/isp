def dfs(node, computers, visited):
    # 방문했다면 종료
    if visited[node] == 1:
        return
    # 방문처리
    visited[node] = 1

    # 방문한곳의 노드탐색
    for i in computers[node]:
        if visited[i] == 0:
            dfs(i, computers, visited)


def solution(n, computers):
    new_c = [[] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                new_c[i].append(j)
    visited = [0] * n
    cnt = 0
    for i in range(n):
        # 방문을 안했을시
        if visited[i] == 0:
            dfs(i, new_c, visited)

            cnt += 1
    return cnt
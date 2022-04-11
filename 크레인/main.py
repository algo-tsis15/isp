def solution(board, moves):
    n = len(board)
    d = [[] for i in range(n)]
    basket = []

    for i in range(n):
        for j in range(n):
            if board[n - j - 1][i] == 0:
                break
            d[i].append(board[n - j - 1][i])

    cnt = 0
    for i in moves:
        if len(d[i - 1]) == 0:
            continue
        # 바구니가 비어있지 않을시 적합성 검사
        if len(basket) != 0:
            if basket[-1] == d[i - 1][-1]:
                basket.pop()
                d[i - 1].pop()
                cnt += 2
            else:
                basket.append(d[i - 1].pop())
        # 비어있을시
        else:
            basket.append(d[i - 1].pop())

    return cnt
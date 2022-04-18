global answer
answer = 0


def dfs(d, c_num, numbers, target):
    global answer

    if d == len(numbers):
        if c_num == target:
            answer += 1
        return

    c_num += numbers[d]
    dfs(d + 1, c_num, numbers, target)
    c_num -= numbers[d]
    c_num -= numbers[d]
    dfs(d + 1, c_num, numbers, target)
    c_num += numbers[d]


def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer
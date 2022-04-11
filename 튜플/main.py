import copy

def solution(s):
    s = list(s)

    new_s = []
    num = []
    tmp = ""
    for i in range(len(s) - 2):
        if s[i].isdigit():
            tmp += s[i]
            if s[i + 1] == ',':
                num.append(int(tmp))
                tmp = ""
            elif s[i + 1] == '}':
                num.append(int(tmp))
                new_s.append([len(num), copy.deepcopy(num)])
                tmp = ""
                num.clear()
    new_s.sort()
    result = []
    for i, n in new_s:
        for j in range(i):
            if n[j] not in result:
                result.append(n[j])
    return result
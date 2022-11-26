def solution(n):
    answer = []
    num = 2
    while n != 1:
        if n%num == 0:
            answer.append(num)
            n = n//num
            num = 2
        else :
            num = num + 1

    return sorted(list(set(answer)))

n = 35
print(solution(n))
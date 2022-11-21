def solution(my_str, n):
    answer = [my_str[n*i:n*(i+1)] for i in range((len(my_str)//n)+1) if my_str[n*i:n*(i+1)] != '']
    return answer


my_str = "abc1Addfggg4556b"
print(solution(my_str,4))
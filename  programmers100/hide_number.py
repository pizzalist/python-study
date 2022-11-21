#숨어있는_숫자의_덧셈(2)

#문자열 my_string이 매개변수로 주어집니다. 
# my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
# my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
import string
def solution(my_string):
    for alphabet in list(string.ascii_letters):   
        my_string = my_string.replace(alphabet," ")
    list_my = list(filter(None, my_string.split(" ")))
    list_my_int = list(map(int, list_my))
    return sum(list_my_int)


my_string = "as120asdfdf"
solution(my_string)
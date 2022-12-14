# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    
    
    try:
        int(user_input_number)
        result = True 
    except ValueError:
        result = False

    # ==================================
    return result

# "123".isdigit()

    

def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    change_to_int = int(user_input_number)
    if change_to_int >= 100 and change_to_int<1000:
        result = True 
    else: 
        result = False
    # ==================================
    return result
# change_to_int 함수 이름 같다.


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # Hint - Len과 Set을 써서 할 수 있음, 중복되는 값의 str 길이는 1 또는 2
    num_list = list(three_digit)    #list는 iteror한 객체라서 없어도 된다.
    num_set = set(num_list)
    if len(num_set) == 3: 
        result = False
    else:
        result = True

    # ==================================
    return result



def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if is_digit(user_input_number) and \
       is_between_100_and_999(user_input_number) == True and \
       is_duplicated_number(user_input_number) == False:  
        result = True
    else:
        result = False
    # ==================================
    return result
# 일관성 있게 쓰자.
#논리 연산자 순서 공부


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # get_random_number() 함수를 사용하여 random number 생성
    random_num = str(get_random_number())
    while is_duplicated_number(random_num) == True: #TRUE 도 지워도됨
        random_num = str(get_random_number())
        # 밑에 두줄 없어도 됨
        if is_duplicated_number(random_num) == False:
            break
    result = random_num
    # ==================================
    return result



def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    

    #문자열 값을 리스트로 옮긴다
    input_list = list(user_input_number)
    random_list = list(random_number)   
    #리스트 비교하여 숫자와 위치가 같은 것을 strike_num 리스트에 담는다
    strike_num = []
    for input_num, random_num in zip(input_list, random_list):
        if input_num == random_num:
            strike_num.append(input_num)
    #기존 리스트들에서 strike된 숫자는 remove
    # input_list.remove(input_num)
    for i in strike_num:
        input_list.remove(i)
    for i in strike_num: #지워도 됨
        random_list.remove(i)


    # set으로 변경 시켜서 같은 문자 찾아서 ball 리스트에 담는다
    ball_num = []
    for i in input_list:
        for j in random_list:
            if i == j:
                ball_num.append(i)




    #갯수 리스트로 만든다.
    result = [len(strike_num),len(ball_num)]
    # ==================================
    return result



def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if one_more_input.lower() == "y" or \
        one_more_input.lower() == "yes":
        
        result = True
    else: 
        result = False
    # ==================================
    return result



def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if one_more_input.lower() == "n" or \
        one_more_input.lower() == "no":
        result = True
    else: 
        result = False
    # ==================================
    return result




def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    # ===Modify codes below=============
    # 위의 코드를 포함하여 자유로운 수정이 가능함
    def start(user_input):
        user_input = str(input('Input guess number : '))
        if user_input == '0':
            exit()
        while is_validated_number(user_input) == False:
            user_input = str(input('Wrong Input, Input again : '))
            if is_validated_number(user_input) == True:
                break
        
        strike, balls = get_strikes_or_ball(user_input, random_number)
        while True :
            print("Strike :",strike,"Balls :", balls)
            if strike !=3:
                start(user_input)
            if strike == 3 :
                break
        
        one_more = input('You win, one more(Y/N) ?')
        
        if is_yes(one_more) == True:
            main()
        elif one_more == '0':
            exit()
        elif is_no(one_more) == True:
            print("Thank you for using this program")
            print("End of the Game")
            exit()
        else:
            while True:
                one_more = input('Wrong Input, Input again : ')
                if is_yes(one_more) == True:
                    main()
                elif one_more == '0':
                    exit()
                elif is_no(one_more) == True:
                    break
    start(user_input)
    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()

# baseball 코드 리뷰 
> 22.11.13 진행 <br>
> baseball 과제 코드 리뷰<br>
> [원본 코드 링크 및 관련 자료](https://github.com/pizzalist/python-study/tree/main/lab_7)
+ isdigt()으로 문자열이 숫자로만 구성되어있는지 판별
```python
str = '1234'
print(str.isdigit())
# True

str = 'abc1234'
print(str.isdigit())
#False
```
isdigit()은 문자열의 구성 요소가 모두 숫자인지 확인하는 함수입니다. 문자열에 +나 - 같은 부호가 있다면 숫자가 아니기 때문에 isdigit()은 false를 리턴합니다. 또한 소수점도 숫자가 아니기 때문에 false가 리턴

> ## 원래 코드
```python
change_to_int = int(user_input_number)
    if change_to_int >= 100 and change_to_int<1000:
        result = True 
    else: 
        result = False
    # ==================================
    return result
```
> ## review 받은 수정 코드
```python
user_input_number = int(user_input_number) 
    return user_input_number >= 100 and user_input_number < 1000
```
위와 같이 True, False 값 if문으로 안해줘도 값 나온다!

---
> ## 원래 코드
```python
num_list = list(three_digit)    #list는 iteror한 객체라서 없어도 된다.
num_set = set(num_list)
if len(num_set) == 3: 
    result = False
else:
    result = True

# ==================================
return result
```

+ list는 iteror한 객체라서 없어도 된다.
---
> ## 원래 코드
```python
if is_digit(user_input_number) and \  # ==True 빠짐
    is_between_100_and_999(user_input_number) == True and \
    is_duplicated_number(user_input_number) == False:  
    result = True
else:
    result = False
# ==================================
return result
```
>## 수정 코드
```python
if is_digit(user_input_number) != True:
    return False

if is_between_100_and_999(user_input_number) != True:
    return False

if is_duplicated_number(user_input_number) != False:
    return False

return True
```
+ 일관성 있게 코드를 작성하자.
+ 논리 연산자 순서에 대해 공부하자
  

---
>## 원래 코드
```python
random_num = str(get_random_number())
    while is_duplicated_number(random_num) == True: #TRUE 도 지워도됨
        random_num = str(get_random_number())
       
        # 밑에 두줄 없어도 됨
        if is_duplicated_number(random_num) == False:
            break
    result = random_num
    # ==================================
    return result
```
---
>## 원래 코드
```python
input_list = list(user_input_number)
random_list = list(random_number)   
strike_num = []
for input_num, random_num in zip(input_list, random_list):
    if input_num == random_num:
        strike_num.append(input_num)
for i in strike_num:
    input_list.remove(i)
for i in strike_num: #지워도 됨
    random_list.remove(i)


ball_num = []
for i in input_list:
    for j in random_list:
        if i == j:
            ball_num.append(i)

result = [len(strike_num),len(ball_num)]
# ==================================
return result
```

>## 다른 방법 1
```python
input_list = list(user_input_number)
random_list = list(random_number)   
strike_num = []
for input_num, random_num in zip(input_list, random_list):
    if input_num == random_num:
        strike_num.append(input_num)
for i in strike_num:
    input_list.remove(i)
for i in strike_num: #지워도 됨
    random_list.remove(i)

# 2) set 을 사용한다
balls = set(input_list) & set(random_list)
len(balls)
```
set 을 이용한다.
  + set은 고유한 값을 가진다. (값 중복 불가능)
  
    ### | => or union 합집합
    ### & or difference => and
    ### - => 차집합
    ### + => 합집합

>## 다른 방법 2
```python
strikes = sum([n1 == n2 for n1, n2 in zip(user_input_number, random_number)])
balls = len(set(user_input_number) & set(random_number))

return [strikes, balls - strikes]
```
+ 반복문을 활용하여 스트라이크의 숫자들의 갯수를 모두 더한 스트라이크를 구해준다.
+ 그리고 교집합의 개념을 이용하여 그 갯수를 볼로 구한다.
+ 볼에서 자리가 같은 스트라이크의 갯수를 빼준다.
>## 다른 방법 3
```python
strike_num = 0
ball_num = 0
for input_num, random_num in zip(user_input_number, random_number):
    if input_num == random_num:
        strike_num += 1
        # strike_num.append(input_num)
    elif input_num in random_number:
        ball_num += 1
        # ball_num.append(input_num)

result = [strike_num, ball_num]
```

---
>## 원래 코드
```python 
def main():
    print("Play Baseball")
    user_input = 999
    while True:
        random_number = str(get_not_duplicated_three_digit_number())
        print('Random Number is : ', random_number)
        user_input = str(input('Input guess number : '))
        strike, balls = get_strikes_or_ball(user_input, random_number)
        # ===Modify codes below=============
        # 위의 코드를 포함하여 자유로운 수정이 가능함
        
        while strike !=3:
            if is_validated_number(user_input) == True:
                print("Strikes :",strike,",","Balls :", balls)
                user_input = str(input('Input guess number : '))
                strike, balls = get_strikes_or_ball(user_input, random_number)
            elif user_input == '0':
                break

            elif is_validated_number(user_input) == False:
                print('Wrong Input, Input again')
                user_input = str(input('Input guess number : '))
                strike, balls = get_strikes_or_ball(user_input, random_number)
        if user_input == '0':
            break
        else:
            print("Strikes :",strike,",","Balls :", balls)

        one_more = input('You win, one more(Y/N) ?')
        while is_yes(one_more) == False and is_no(one_more) == False :
            # and one_more !='0':
            print('Wrong Input, Input again')
            one_more = input('You win, one more(Y/N)?')
        if is_no(one_more) == True:
            break   
        
        # 생략 가능
        # elif is_yes(one_more) == True:
        #     pass

```


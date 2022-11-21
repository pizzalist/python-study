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
>## 수정 코드 1
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

# 1) in 조건을 쓴다
ball_num = []
for i in input_list: 
    if i in random_list:
        ball_num.append(i)
```
in 조건을 사용한다
>## 수정 코드 2
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
### | => or = 합집합
### & => and
### - => 차집합
### + => 합집합
>## 다른 방법
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
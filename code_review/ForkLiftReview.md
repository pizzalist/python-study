# teamlab_forklift_ds 코드 리뷰 
> 22.11.06 진행 <br>
> 알고리즘과 자료구조 수업 과제 ForkLiftList 과제 코드 리뷰<br>
> [원본 코드 링크 및 관련 자료](https://github.com/pizzalist/dsaa-2022/tree/main/dsaa/teamlab_forklift_ds)
+ load_dataset 함수
> ## 원래 코드
```python
data_header = []
    for i in range(len(command_data)):
        if i == 0:
            continue
        if command_data[i][1] not in data_header:
                data_header.append(command_data[i][1])  

    dataset = {}
    for i in range(len(data_header)):
      dataset[data_header[i]] = []

    dataset_list = []
    for i in range(len(data_header)):
        for j in range(len(command_data)):
            if data_header[i] == command_data[j][1]:
                dataset_list.append(command_data[j][3])
                dataset_list.append(command_data[j][4]) 
                dataset_list.append(command_data[j][2])
                dataset[data_header[i]].append(dataset_list)
                dataset_list = []
```
> ## review 받은 수정 코드
> 
```python
command_data = []
    with open (filename, "r") as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in datareader:
            command_data.append(row)
    
    dataset = {}
    for data in command_data[1:]:   #for 뒤 부분에 i 가 아닌 data라는 명확한 이름을 정해줌 
        fork_id, in_dt, emp_x, emp_y = data[1:] #데이터 언팩킹 사용
        if fork_id not in dataset:
            dataset[fork_id] = []
        dataset[fork_id].append([emp_x, emp_y, in_dt])
```
**수정사항**
+ 변수명 신경쓰기

+ 파일의 데이터를 불러올때 인덱스 보다는 파일 시트 이름으로 불러와서 **데이터 언패킹** 사용
  <ul> 데이터 언패킹(unpacking) : 시퀀스를 개별 아이템으로 나누기
```python
    s = 'Hello'
    a, b, c, d, e = s

    print(a) #-> 'H'
    print(b) #-> 'e'
    print(c) #-> 'l'
    print(d) #-> 'l'
    print(e) #-> 'o'

    # 언패킹할 때 특정 값을 무시하고자 하는 경우에는,
    # 관례적으로 _ 또는 ign(ignored) 변수를 사용한다.
    data = ['foo', 'bar', 'baz']
    x, _, y = data
    print(x) #-> 'foo'
    print(y) #-> 'baz'

    # *사용으로 요소 여러개 묶기 
    data = ('a', 'b', 'c', 'd')
    x, *y = data
    print(x) #-> 'a'
    print(y) #-> ['b', 'c', 'd']

    # 중간값을 버리고 앞/뒤 값만 취하고 싶을때
    data = ('first', 80, 'foo', 'bar', 'last')
    head, *_, tail = data
    print(head) #-> 'first'
    print(tail) #-> 'last'
    # 평균 구할때도 사용 가능
```
  </ul>


  


> ## defaultdict 사용
```python
command_data = []
    with open (filename, "r") as csvfile:
        datareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in datareader:
            command_data.append(row)
    dataset = defaultdict(list)
    for data in command_data[1:]:
        fork_id, in_dt, emp_x, emp_y = data[1:]
        dataset[fork_id].append([emp_x, emp_y, in_dt])
```
---
+ sort_dataset 함수
> ## 원래 코드
```python
for i in dataset.keys():
        sorted_dataset = dataset
        sorted_dataset[i] = sorted(dataset[i], key=lambda x : x[2])
    
    return sorted_dataset
```

> ## 수정 코드
```python
sorted_dataset = {}
    for key in dataset.keys():  #i 는 인덱스이기 때문에 명확한 이름 올 필요가 있다.
        # sorted_dataset = dataset      왜 ?? 메모리 사용 공간 더 잡아먹음 : 지우기 
        sorted_dataset[key] = sorted(dataset[key], key=lambda x : x[2])
```
수정 사항
<ul>
<li>i 는 인덱스의 줄임말로 다음과 같은 key값들을 불러오는 경우에는 key라고 명확한 네이밍을 하는 것이 보기 좋다.
<li>똑같은 것을 변수로 중복 할당 해주고 있는데 이는 메모리 사용 공간을 더 잡아먹으므로 지우는 것이 좋다.
</ul>

> ## 원래 코드
```python
a = sorted_dataset #모르는 변수 지정 지향
keys_list = list(sorted_dataset.keys()) # list 제외 가능 ((iterator))
linkedlist_bag_dict = {}

    
for i in keys_list: # TEAM..., 
    linkedlist_bag_dict[i] = LinkedListBag()
    for j in a[i] : # ['172978.787361283','252229.400114715','2019-06-01 08:30:48.797'] ['172978.787361283','252229.400114715','2019-06-01 08:30:48.797']
        linkedlist_bag_dict[i].append(ForkliftNode(i, float(j[0]), float(j[1]), datetime.strptime(j[2], "%Y-%m-%d %H:%M:%S.%f")))

  
    return linkedlist_bag_dict
```
> ## 수정 코드
 ```python
linkedlist_bag_dict = {}
for fork_id in sorted_dataset.keys(): # TEAM..., 
    linkedlist_bag_dict[fork_id] = LinkedListBag()
    for emp_x, emp_y, in_dt in sorted_dataset[fork_id] : 
        emp_x  = float(emp_x)
        emp_y  = float(emp_y)
        in_dt  = datetime.strptime(in_dt, "%Y-%m-%d %H:%M:%S.%f")
        linkedlist_bag_dict[fork_id].append(ForkliftNode(fork_id, emp_x, emp_y, in_dt))
```
+ 수정 사항
  <ul> 모르는 변수 지정 지향 </ul>
  <ul> list 제외 가능하다 (iterator 개념 공부) </ul>
  <ul> 앞 코드와 마찬가지로 데이터 언패킹사용으로 복잡하지 않게 ! </ul>
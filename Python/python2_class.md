# Python2_class

## 자료형

### 원시 자료형



- 불린형(Boolean Type)

True / False 대문자로 써야함 

bool(0) : 리턴 값 :  False

비어있는 것은 : False / 나머지 : True



- 수치형(Numeric Type)

```python
a = 2 ** 64
type(a)
```

2의 64제곱도 int이다.

파이썬에는 담을 수 있는 그릇의 크기가 존재하지 않는다. 



- 부동소수점

```python
round(x,2)

** 이 코드가 좋음(알아보기 쉬움) **
import math
math.isclose(a, b)

=> 알아서 판별해주겠다는 함수
```



- 복소수(Complex number)

-> 쓴적은 없으시다



- 문자열(String Type)

(Pick a rule and Stick to it)

Immutalbe : 변경할 수 없음

```python
a = 'boxes'
a[-1]
=> s 출력됨
```

'boxes'가 [ 'b', 'o', 'x', 'e', 's'] 로 저장되어있음 



- String interpolation

```python
name = '염'
score = '100'
print('{}의 성적은 {}입니다.'.format(name, score))

*** 파이써닉한 코드 *** (fstring)
print(f'{name}의 성적은 {score}입니다.')

{pi:.3} 소수점 둘째 자리 까지
pi = 3.141592
print(f'원주율은 {pi:.3}. x 2 = {pi * 2}')
```

`f`를 넣어주는 것이 핵심 `f-string`

{}안에 int, float, string, list 전부 대입 가능 ! 

fstirng dataformat



- None Type

알고리즘 문제 쓸 때 사용함





### 컨테이너 

여러개의 값을 저장할 수 있음을 의미함

시퀀스 : 리스트. 튜플, 레인지

비시퀀스 : 세트, 딕셔너리 



- 리스트

```python
my_list = []
another_list = list()
print(my_list , another_list)

(2차원 리스트: 리스트 안에 리스트)
boxes =['A', 'B', ['apple', 'banana', 'cherry']]
```

***리스트는 반드시 변수명을 복수형으로 작성***

Positive index[0] ~ 

Negative index[-1] ~

```python
boxes[1] = 'C'
print(id(boxes), boxes)
boxes[1] = 'D'
print(id(boxes), boxes)
```





- 튜플(Tuple)

튜플임을 표현하려면  뒤에 `, ` 찍어줘야 함 

```python
empty()
비어있는 튜플 만들기 
```



- 레인지(range())

정수의 시퀀스 

진짜 범위를 의미하는게 아님 / 정수는 정

기본형 : range(n) 0부터 

범위지정 : range(n, m) n부터 m-1까지 

범위 및 스탭 : range(n, m, i)



n이 시작점 , m이 끝점 스탭이 없으면 +1과 같음 



```python
list(range(100, 0, -10))
=> 왼쪽으로 가겠다는 뜻
```

마지막 것은(m) 포함하지 않는다는 의미 

```py
ran
```

- 패킹 / 언패킹 연산자 





- 세트

활용 가능한 연산자는 차집합(`-`), 합집합(`|`), 교집합(`&`)입니다

빈셋 set()

```python
locations= ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산' ]
print(locations)
set(locations)
print(len(set(locations)))
```

순서가 다르게 나올 가능성이 있음 -> 인덱스 접근 불가



- 딕셔너리

빈 딕셔너리 {}

내부에 들어가있는 모양새에 따라서 set/dictionary가 다르게 

key = `스트링` 사용해야하는 것을 권장함

value = list, dict, 등 다 사용 가능

파이썬 3.6부터는 순서를 보장해 줌 

```python
d1 = []
di2 = dict()
phone_book = {'서울': '02', '경기': '031', '인천': '032'}

phone_book.keys()
phone_book.values()
phone_book.items()
```



### 형변환

의도하지 않은 형변환으로 뭘 할 생각을 하지 마세요 

EX) True + 99 

```python
int_number + float_number 
```



Invalid literal for int() with base 10 :'hi' 

=> 10진수일 경우에만 변환 가능하다. 



### 컨테이너 형 변환

<튜플 / 셋 / 리스트> 

차이점 : 할 수 있는 행동이 다름





{} 중괄호 있는 애들은 순서 x

[], () 쓰는 애들은 순서가 있음 



list 를 잠근 것 tuple

{} 중괄호 있는 애들만 mutable 변경 가능

나머지 String, range는 변경 불가능 



### 산술 연산자

```python
2 ** 10
2의 10승

10 // 5
10을 5로 나눈 몫

11 % 10 
11을 10으로 나누고 남은 나머지 

divmode(5, 2) => (2,1)
Q = divmod[0]
R = divmod[1]
print(f'몫은 {Q}, 나머지는 {R}')
5를 2로 나눈 몫과 나머지를 출력

positive_num = 4
print(-positive_num)
```



### 비교 연산자

```python
x = 3
x is None
```



### 논리 연산자

and , or , not



### 복합연산자

`+=` , `-=`. `*=`, `/=`, `//=` , `%=`, `**=`

`=` 이 무조건 뒤에 있다.



## 슬라이싱

``` python
print(range(10)[5:8])
=> range(5, 8)

print([1,2,3,4][0:4:2])
=> [1, 3]

print(s[::])
=> 처음부터 끝까지

***
print(s[::-1])
=> 역순으로 정렬 
```



## 연산자 우선순위

0. `()`을 통한 grouping

1. Slicing

2. Indexing

3. 제곱연산자
    `**`

4. 단항연산자 
    `+`, `-` (음수/양수 부호)

5. 산술연산자
    `*`, `/`, `%`
    
6. 산술연산자
    `+`, `-`

7. 비교연산자, `in`, `is`

8. `not`

9. `and` 

10. `or`










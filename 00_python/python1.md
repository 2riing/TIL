# 파이썬

## 서론

컴퓨터에게 말하는 약속

- 선언적 지식

  사실에 대한 내용 

- 명령적 지식

  "HOW - to "



##  파이썬 개발환경

간결하게 작성 가능한 파이썬 



### 파이썬 개발환경 종류

- 대화형 환경 (주피터) => 실습 
- 스크립트 실행 (.py 파일을 통해 IDE활용) => 금요일/평가



IDEL(파이썬 기본 인터프리터)

Jupyter Lab ()

IDE(통합 개발 환경) : Pycharm

Text editor(메모장 확장판) : VS code



### 코드 스타일 가이드

파이썬에서 제안하는 스타일 가이드 - PEP8

기업 오픈소스에서 사용되는 스타일 가이드 



띄어쓰기와 '잘쓰기

변수명 잘 설정하기 



## 기초문법

### 변수

type() :변수에 할당된 값의 타입

id() : 변수에 할당된 값의 메모리 주소 



### 변수 할당

```python
x = y = 20000
```

같은 값 동시에 할당 가능



```python
x, y = 1, 2
```

다른 값을 동시에 할당 가능



``` python
x, y = 1
```

TypeError : cannot unpack non-iterable int object

=> 풀 수 없었다



``` python
x, y = 1, 2, 3
```

ValueError : too many values to unpack 

=>너무 많은 값들이 있어



```python
x, y = 10, 20
tmp = x
x = y
y = tmp
print(x,y)

y, x = x, y
```

x-y의 값을 바꾸는 방법 Pythonic한 코드 





### 변수 이름 짓는 방법

- 대소문자 구별함

- 사용할 수 없는 키워드 존재

- 알파벳, _, 숫자로 구성

- 길이제한 x

-  첫 글자에 숫자 x

ex) red-apple(snake_case), RedApple(camel_case)

~~파이썬은 내장함수가 튼튼하다~~ 



TypeError : strobject is not callabe 

=> 부를 수 없음



### 사용자 입력

~~못들음~~



### 주석

한줄 주석 (#)

여러 줄의 주석 `""" or '''` & `ctrl + /`



## 파이썬 자료형 (Python Datatype)

### 자료형 분류

Boolean Type

Numeric Type (Int, Float, Complex)

String Type



### None

~~왜쓰지?~~~

어떤 값이 없다라는.. 것을 해주기 위해서 사용함

```python
print(type(None))
<class = 'none Type'
```



### Boolean

비어있는 것은 모두 False

0, 0.0 , (), [], {}, '', None



###  INT

모든 정수의 타입은 **int** ~~long 등이 없음~~

특) 매우 큰 수를 나타낼 때 오버플로우가 발생하지 않음. 한계가X

2진수 : 0b (binary)

8진수 : 0o (octo)

16진수 : 0x (hexa)

`BOX`로 암기 ! 앞에 머리말처럼 붙여줌





### Float

정수가 아닌 모든 실수 : **Float**

```python
1e-1
```

0.1



### Floating point rounding error

실수 연산과정에서 오류 발생가능

```python
3.14 - 3.02 = 0.12000000...00001
```

따라서 0.12가 아님

~~..?~~

```python
import math
math.isclose(a, b)
```





### 문자열

 ``` python
 print('주나 "안녕"')
 ```

주나 "안녕"



- Immutalble(불변)

- Iterable

반복 가능

```python
a = '123'
for char in a:
    print(char)
```

1

2

3



### Excape sequence

\n 줄바꿈

\t 탭

\r 캐리지리턴 : 쓸일 거의 없음

\0 널

\\ 백슬래쉬

\\'  \\"



### String Interpolation (문자열 사이에 변수)

%s -> string

%d -> int

%f -> float

```python
print('Hello, {}! 성적은 {}'.format(name, score))
pritn(f'Hello, {name}! 성적은 {score}')
```

=> 맨 마지막꺼를 선호하심 f-string:python 3.6+

```python
f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일'
```

오늘은 21년 06월 24일





### 컨테이너

서로 다른 자료형을 저장할 수 있음

- 순서가 있는 데이터 (Ordered) 시퀀스형

  리스트(가변), 튜플(불변), 레인지(불변) 

- 순서가 없는 데이터 (Unordered) 비 시퀀스형

  세트(가변), 딕셔너리(가변)





### 리스트

생성된 이후 내용이 변경가능한 **가변 자료형** 

```python
my list = []
another_list = list()
location = [1,2,3,4,5]
```

0,1,2,3,4,5,6

-7,-6,-5,-4,-3,-2,-1

시작은 0 끝은 -1

~~아개쩐다~~



```boxes  = ['a', 'b', ['c','d', 'e']]
boxes  = ['a', 'b', ['c', 'd', 'e']]
boxes[2][-1] => e
순서대로 하면 됨
```





### 튜플

생성된 이후 내용이 변경 불가한 **불변 자료형**

```
(1,2,3,4)
tuple((1,2,3,4))
```

하나의 항목으로 구성된 튜플은 생성시 밧 뒤에 쉼표를 붙여야함

``` python
a = 1,
b = 1,2,3
```



튜플은 일반적으로 파이썬 내부에서만 사용 

튜블덕분에 사용이 가능하다. 리스트와의 차이점만 기억

(뭔지는 알고 있는게 중요함)





### 레인지 

***자주 사용됨***

- 기본형 : range(n)

0 부터 n-1까지의 숫자 시퀀스

- 범위지정(n, m)

n이상 m미만 n 부터 m-1까지 

- 범위 및 스텝 지정 range(1, 3, 2) , range(6, 1, -1)



### 패킹/언패킹

- 패킹

```python
x, *y = 1, 2, 3, 4
x => 1
y => [2, 3, 4]
```





### **셋**

중복없이 순서가 없는 자료구조 

```py
{1, 2, 3, 1, 2} => {1, 2, 3}
set() -> 빈 set
{} -> empty 딕셔너리 
```

순서가 없기 때문에 인덱스로 접근 불가능함



``` python
len(set(my_list))
```

**중복되는 것을 제거하고 개수만 알고 싶을 때** 엄청 유용함 



### **딕셔너리**

순서 없이 키값의 쌍으로 이루어진 자료형

~~HASH와 비슷함?~~

```python
dict_a = {'a' : 'apple' , 'b' : ['baba', 'babo']}
dict_a['b'][-1] => 'babo'
```

키(key) : 리스트 x

값(value) : 리스트, 문자열 숫자 모두 가능 





### 형 변환(Typecasting)

- 암시적 형변환 (자연스럽게 내부적으로 자료형 변환, Implicit)

  ``` python
  True + 3
  ```

  

- 명시적 형변환 (사용자가 함수를 활용하여 의도적으로 자료형 변환, Explicit)

``` python
str, float => int
str, int => float
int, float, list, tuple, dict => str

int('3')+4 =>7
int('3.5')+4 => ValueError

```





### 연산자

- 산술연산자

// 몫

% 나머지 (홀짝 구분시 사용가능 )

- 비교 연산자 

!= 같지 않음

- 논리 연산자 단축평가 

```python
a = 5 and 4
print(a) => and는 마지막 것까지 확인해야해서 4가 나옴
b = 5 or 4
print(b) => 하나만 True면 바로 5반환
c = 0 and 5
print(c) => 첫번째가 False가 나오는 순간 바로 0 반환
d = 0 or 5
print(d)=> 5를 반환
어디까지 가는지? 를 확인하는 것
```

- 복합 연산자(In-Place Operator)

``` python
cnt += 1
```

- 식별 연산자
- 멤버십 연산자 (Membership Operator)

in

not in

```python
1 in [3,2] => False
'a' in 'apple' => True
```

 - 시퀀스형 연산자

```python
'12'+'b'
'hi' * 3 => 'hihihi'
[0] * 8 => [0, 0, ...]
```

- 인덱싱(중요)

```python
[1, 2, 3][2] => 3
(1, 2, 3)[-1] => 3
```

IndexError : 없는 인덱스에 접근 (너무나 쉬운 에러)

- 슬라이싱

```python
[1, 2, 3, 5][1:4] => [2, 3, 5]
[1, 2, 3, 5][0:4:2] =>2의간격으로 슬라이싱 
 s[:3] => 처음부터 3까지
 s[::] => 그대로 출력 
 s[::-1] => 값을 뒤집고 싶을 때 
```

- 집합

| : 합집합

& : 교집합

\- : 여집합

^ : 대칭차

-  연산자 우선순위

소괄호를 열심히 묶으면 됨




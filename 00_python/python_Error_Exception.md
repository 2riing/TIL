# Python 예외 & 에러처리


## 1. 에러

## 2. 예외

문법적으로 맞지만 상황적으로 불가능

- ZeroDinisionError
- NameError
- TypeError 
sample() missing 1 required positional argument :매개변수 개수가 초과
choice() takes 2 positional arguments but 3 were given : 
- indexError
list index out of range : 인덱스 값을 잘못 입력 함
- IndentationError : 들여쓰기를 잘하자 

## 예외처리
1. try & except & finally 

```Python
try:
    <code>
excopt (예외):
    <code>
```

## 에러 발생 시키기 

패키지나 묘듈을 만들 때 사용할 확률이 큰데, 

raise ValueError('hi')
# Python OOP(Object Oriented Programming)


## 서론 

철학에서 파생된 개념이다.

Python은 모든 것이 객체이다.

이데아, 
"서양 철학은 플라톤의 각주에 불과하다."

class Chair 의자 의 속성 특성을 만듬

그 이후에 의자1, 의자2, 의자3을 만든다. 
[인스턴스: 개별 사례, 예시]




### 객체 중심의 장점 
SW 개발 보수가 편해진다. 


### 객체들의 상호작용 ?

p1.money + p2.money

```python
class Person:
    def __init__(self, h, w, m):
        self.height = h
        self.wight = w
        self.money = m

p1 = Person(180,80,500)
p2 = Person(175, 70, 1000)
```

## 속성과 메서드(핵심)

### 속성

객체.속성

### 메서드

객체.메서드()


## 인스턴스

### self

p1이 자동으로 self 자리로 들어감

### 생성자 메서드 

### 소멸자(destructor) 메서드
# Python OOP(Object Oriented Programming.)


## 서론 

철학에서 파생된 개념이다.

Python은 모든 것이 객체이다.

이데아, 
"서양 철학은 플라톤의 각주에 불과하다."

class Chair 의자 의 속성 특성을 만듬

그 이후에 의자1, 의자2, 의자3을 만든다. 
[인스턴스: 개별 사례, 예시]

모든 객체는 자신만의 속성과 움직임을 가질 수 있다. 




## 객체와 인스턴스

객체(Object) : 실존하는 모든 것

인스턴스(Instance) : 특정 클래스의 인스턴스 이다. 

객체 == 정수 객체 == int class의 인스턴스 

파이썬에서는 모든 객체가 인스턴스이다. (아닌 언어도 있음)

* int라는 클래스 자체도 인스턴스 인가..?



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

Person() : Person 클래스의 인스턴트 생성
-> 생성하고 나면 함수의 실행이 

### self

p1이 자동으로 self 자리로 들어감

알아서

### 생성자 메서드 

### 소멸자(destructor) 메서드


## 속성 

p1 = Person('ssafy')

p1.talk()




## 매직(스페셜) 메서드

init메서드가 없어도 초기 선언 가능하다. 

이미 많은 스페셜 메서드들이 사용가능

이유: 더 상위의 클래스에서 받아오고 있기 때문에 



__str__ : print(p1) => 출력 (남에게 보여지는 값을)

__repr__ : p1 => 출력 (어떤 값을 리턴할 것인가?)

__gt__ : greater than

(1).__gt__(2)
```python
def __gt__(self, other):
    return self.age > other.age
```

연산자도 메서드로 이루어져 있더라..


## 클래스 

 클래스 이름은 Camel 방식으로 
 
 ex) ClassName

 멀티라인 주석 으로 클래스 설명 출력가능 Use `__doc__` 

 Person.__doc__




instance 메서드는 (self(인스턴스본인), ..)

class 메서드는 (cls(클래스본인), ... )


자식을 출력해도 부모 속성을 가져올 수 있다. 

나한테 없으면 부모꺼 가져오지만 나한테 있을 때는 내꺼를 가져온다. 

## 스태틱 메서드

자동으로 어떤 것도 생기지 않는 

호출시 어떠한 인자도 self, cls처럼 자동으로 전달되지 않습니다. 

찐 함수같은 것 ... 

존재의 이유?  

인스턴스와 클래스 method는 self와 cls의 영향을 받지만

속성을 다루지 않고 기능만, 일반 함수와 아주 같음



## 주의사항

인스턴스가 할 행동은 인스턴스 매서드로 한정 지어서 설계 

부모 자식간에 접근 가능하지만 굳이 사용하지 않는다.

`올바른 예`

```python 

MyClass.class_method()
MyClass.static_method()
```


## OOP의 핵심 개념

객체지향이 무엇을 위해서 태어났는가? 객체지향의 장점

### 추상화

현실 세계를 설계에 반영하기 위해서 사용 되는 것.

Person = Professor + Student

### 상속

Person 클래스를 상속받아서 Student를 만들 수 있다. 

모든 class는 type에서 부터 온다 

Metaclass

super()

### 다형성

- 메서드 오버라이딩 : 덮어쓰기 

### 캡슐화 

외부에서 직접적인 액세서를 차단하는 것

JAVA는 엄격하게 구분을 해놨으나, 파이썬은 유연함 

- Public Member
- Protected Member
- Private Member


메서드가 상속하는 순서에 따라서 
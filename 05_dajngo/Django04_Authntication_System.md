# Django Authentication system

## Authentication System 1
### The Django Authentication System
필요한 모든 것은` settings.py` 에 이미 포함되어있음

`django.contrib.auth` : 인증 프레임워크의 핵심과 기본 모델을 포함

`django.contrib.contenttypes` : 사용자가 생성한 모델과 권한을 연결할 수 있음



인증(Authentication)과 권한(Authorization)부여를 함께 제공하며 

`인증시스템`이라고 부른다.



- Authentication(인증) : 신원확인, 사용자가 누구인지 확인
- Authorization(권한, 허가) : 권한부여, 인증된 사용자가 수행할 수있는 작업을 결정



<두번 째 앱 생성>

$ python manage.py satrtapp accounts



### 쿠키와 세션

#### HTTPS(Hyper Text Transfer Protocol Secure) 

#### HTTP의 특징

- 비연결 지향(connectionless)
- 무상태(stateless) : 연결을 끊는 순간 서버간의 통신이 끝나며 상태정보 유지X

=> `클라이언트`와 `서버`의 지속적인 관계를 유지하기 위해 `쿠키`와 `세션`이 존재 ! 



#### 쿠키

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각 

- 사용자의 컴퓨터에 설치(placed-on)되는 작은 기록 정보 파일

- `KEY & VALUE`형태로 저장

- 재요청 할때 쿠키도 함께 전송함

- 상태가 있는 세션을 만들어줌

- 사용자의 로그인 상태 유지 가능

- 상태가 없는 HTTP프로토콜에서 상태정보를 기억시켜줌

  => 최초에 서버로부터 `쿠키`를 받아서, 그 이후에는 클라이언트가 `요청 + 쿠키`를 보냄 !





#### 쿠키의 사용 목적

1. 세션관리(로그인, 아이디 자동완성, 공지 하루 안보기, 장바구니)
2. 개인화(선호와 테마설정)
3. 트래킹(사용자의 행동 기록 및 분석)



#### 세션

- 클라이언트가 서버에 접속하면 서버가 `session id`를 발급
- `session id`에 알맞은 로직을 처리

=> 로그아웃 : 세션을 삭제하는 것



#### 쿠키의 수명

1. Session Cookie : 세션이 종료되면 삭제됨
2. Persistent cookies : 지정된 날짜or지점에 삭제



#### Session in Django

- 세션은 미들웨어를 통해 구현됨
- db에 저장되고, 저장 방식 변경 가능
- `django_session`테이블에 저장됨
- 모든 것을 세션으로 하면 서버에 부하걸림



#### Authentication System in MIDDLEWARE

- SessionMiddleware : 세션관리
- AuthenticationMiddleware:세션으로 사용저와 연결



### 로그인

`session`을 `Create`하는 로직과 같음



#### 로그인 함수

login(request, user, backend=None)

- 인증된 사용자가 있는 경우
- view함수에서 사용됨
- `from django.contrib.auth import login`

```python
if form.is_valid():
	login(reques, form.get_user())
    return redirect('articles:index')
```



현재 로그인 되어있는 유저 정보 출력 base.html

```python
Hello, {{ user }}
<a href={% url 'accounts:login' %}>Login</a>
```



#### context processor

템플릿이 렌더링 될 때 자동으로 호출 가능한 컨텍스트 데이터 목록

`settings.py` - `Templates`

- Users : 현재 로그인한 사용자를 나타내는 변수 



### 로그아웃

세션을 Delete하는 로직과 같음

#### logout(request)

- 반환값이 없음

``` python
def logout(request):
    logout(request)
    return redirect('articles:index')

<form action="{% url 'account:logout'%}" method = 'POST'>
csrf_token
</form>
```



### 로그인 사용자에 대한 접근 제한

#### Limiting access to logged-in users

1. The raw way : `is_authenticated` attribute
2. Decorator : `login_required`

## Authentication System 2
### 회원가입

### 회원탈퇴

### 회원정보 수정

### 비밀번호 수정









## import

```python
from django.contrib.auth.decorators import login_required


# 회원가입 Form
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

# 로그인 Form
from django.contrib.auth.forms
```




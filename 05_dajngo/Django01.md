# Django
## Web framework

### 용어 - 웹서필할 때 동작하는 것들

* **클라이언트**

웹브라우저(크롬)

* **서버**

diango로 서버를 구축할 것

*  **요청**

www.naver.com입력  : 네이버라는 페이지를 줘 ! (요청)

* **응답** 

네이버 웹페이지를 응답해줌

- 웹서버

http 라는 프로토콜로 들어오는 것이 web임.

웹서버 : 요청이 들어왔을 때 응답을 해주는 것

- framework (틀/일)

틀에 박힌 일만 하면 된다. 

안쓰는 곳 거의 없다..

### 정의

파이썬 Web Framework

수레바퀴를 다시 만들 필요 없이 앱을 만드는데 집중할 수 있다. 

### Static web pasge(정적웹페이지)

서버에 미리 저장된 파일이 `추가적인 처리 없이` 그대로 전달되는 웹페이지

ex) 매일 같은 떡볶이..

### Dynamic web page(동적 웹페이지)

방문자와 상호작용 하기 때문에 페이지 내용은 그때그떄 다름

서버 사이드 프로그래밍언어(Python, Java, C++ 등)가 사용된다.

파일을 처리하고⭐ ***DB와 상호작용***이 일어남

ex) 떡볶이 주세요 안맵게요, 로그인하는 것

### Framework

표준 구조를 구현하는 클래스와 라이브러리 모음

코드를 재사용할 수 있도록 도움

### Web Framework

**개발하는 과정에서 겪는 어려움을 줄이는 것이 주 목적**

기능 : DB연동, 템플릿형태의 표준, 세션관리, 코드 재사용

### Framework Architecture

MVC Design Pattern(model-view-controller)

대부분의 프레임 웍이 MVC디자인 패턴을 따르고 있음

장고는 `MTV Pattern`이라고 함

장고의 개발자들이 

view-> template 

controller->view

라고 부르고 싶어했음

### MTV Pattern

- Model

응용 프로그램의 데이터 구조를 정의하고 DB기록을 관리(추가, 수정, 삭제)

- Template(기본 프레임워크에서는 View)

실제 내용을 보여주는 데 사용(presentation)

- ***View(Controller)*** ⭐가장 중요함⭐

HTTP 요청을 수신하고, 응답을 반환

Model과 의 소통

Template에게는 응답의 서식 설정을 맡김



<MTV 패턴 순서>

HTTP 요청

URL

View(필요시 템플릭, 모델과 소통)

HTTP 응답



~~오늘은 model은 안배움, 해야할게 많습니다.~~



## Django Intro

### 가상환경 설정

$ python -m venv venv

활성화

$ source venv/Scripts/activate 

python interpreter

####  [참고]LTS (Long Term Support)

Long Term Support (장기 지원 버전)

장고의 3.2버전이 안정적인 장기 지원버전이다. 

### 프로젝트 설정

프로젝트 이름

아이픈도 사용X

키워드X

### 프로젝트 구조

`\_\_init.py\_\_` ❌

Python 에게 이 디랙토리를 하나의 패키지로 다루도록 지시 

건드릴 일 없음

`asgi.py` ❌

배포할 때 사용하는 것 . 건드릴 일 없음

**`setting.py` **⭐

애플리케이션의 모든 설정을 포함. 사용할 일 많음

**`urls.py`** ⭐

사이트의 url과 적절한 views의 연결을 지정

요청을 담당하는 파일!

`wsgi.py` ❌

AWS라던지, 서버에 배포할 대 사용하는 것

사용 X

`manage.py` ❌ `a.k.a. 집사`

$ python manage.py <command> [option]

장고 프로젝트와 다양한 방버으로 상호작용하는 커맨드라인 유틸리티 

파일을 터치 X

<command> : ex) runserver

### Aplication 구조

$ ***python manage.py*** strartapp articles

뒤쪽의 명령어만 바뀌는 구조입니다.

**`admin.py`** 

관리자용 페이지를 설정하는 것

`apps.py` ❌

수정X 앱의 정보가 작성된 곳

**`model.spy`** ⭐

앱에서 사용하는 Model을 사용하는 곳

다음 주 부터 본격적으로 사용 예정

`test.py` ❌ 

프로젝트의 테스트 코드를 작성하는 곳

수업에서는 X

**`views.py`** ⭐

view 함수들이 정의 되는 곳

### Application

- Project : 앱은 여러 프로젝트에 있을 수 있음
- Application : 실제 요청을 처리한다. 1프로젝트 多앱, 일반적으로 기능 단위로 작성함

### 앱등록

프로젝트에서 앱을 사용하기 위해서 

`INSTALLED_APPS` 리스트에 추가 필요 ! 

INSTALLED_APPS : 이런 앱을 만들어서 쓸거야. 등록

project file - settings.py - INSTALLED_APPS = [ ]

**주의사항** *선생성 후등록*

앱에 먼저 등록하고 생성하면 앱이 생성되지 않음.

#### [참고]장고 루틴

1. 가상환경 생성 및 활성화
2. django설치 ( $ pip install django==3.2.12 )
3. 프로젝트 생성
4. 서버 켜서 로켓 확인하기
5. 앱 생성
6. 앱 등록

## 요청과 응답

### URL

`url.py`

$ python managy.py runserver

path('admin/', admin.site.urls)

end슬래시를 꼭 붙여줘야함 ! 

```python
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/'m, views.index ),
]
```

trailing comma : 리스트 뒤쪽에 써주는 것. 생산성을 높이기 위해서

### View

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

HTTP 요청을 수신하고 응답을 반환하는 함수 작성

render라는 함수는 첫번째 인자를 요청으로 받습니다. 

### Template

템플릿은 자동으로 만들어주지 않는다. 

`app/templates/` 필수 경로 ! 

## 추가설정

LANGUAGE_CODE = 'en-us' -> 'ko-kr'

TIME_ZONE = 'UTC' -> 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

## Template

데이터 `표현`을 제어하는 도구이자 `표현에 관련된 로직`

### Django Template Languate(DTL)

html은 반복과 조건을 쓸 수 없음. 

그 한계를 극복한 것이 DTL

조건, 반복, 변수 치환, 필터 등의 기능을 제공

Python 처럼 if, for을 사용할 수 있지만 **Python 코드로 실행되는 것이 아님**

### DTL Syntax

1. Variale

```python
{{ variable }}
```

render을 사용하여 template파일로 넘겨 사용하는 것. 

dot(.)을 사용하여 변수 속성에 접근할 수 있음.

render()의 세번재 인자로 {'key':value}와 같이 딕셔너리 형태로 넘겨줌

### [참고] 데이터의 흐름에 따른 코드 작성순서

1. URL
2. VIEW
3. TEMPLATE

### [참고] 실습코드

$ mkdir basic_tv

$ cd basic_tv/

$ python -m venv venv

$ code , (vscode 실행)

$ source venv/Scripts/activate (가상환경 실행)

$ pip list (리스트 확인)

$ pip install django ==3.2.12 (장고설치)

$ django-admin startproject basic_tv . (basic_tv라는 플젝폴더 생성)

$ python manage.py runserver (서버 실행)

$ pytho manage.py start app (app_name) (app생성)



## [실습 순서]

1. app생성
2. mater `settings` - `Installed apps`에 생성한 `'app_name'` 추가
3. path('(app_name)/', include('pages.urls')),
4. app- `url.py` 생성
5. url.py에 작성 `from django.urls import path`
6. `from . import views`
7. `urlpatterns =[ ]`
8. path('dinner/\<str:menu>/\<int:num>/', vies.dinner)
9. app - `view.py`에 작성
10. def dinner(request, menu, num):
11. return render(request, 'dinner.html')
12. `pages`-`templates`-`dinner.html` 생성 





BASE_DIR  => 우리의 앱 최상단을 이야기함

BASE_DIR = Path(__file__).resulove().parent.parent

'DIRS' : [BASE_DIR /'templates']





$ mkdir -p templates/galaxy

$ touch urls.py

$ cd ../../../ 

$ cd - (뒤로가기)





안전하게 만드려면 모든 URL을 POST방식으로 만들어야함

단점 : URL을 타고 들어갈 수가 없음.. 

Unifomed 

Resouce

Locator

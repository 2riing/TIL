# Django Model 





## Databse의 기본 구조 

### 스키마(Schema)

DB에서 자료의 구조, 표현방법, 관계에 관련한 전반적인 명세를 기술한 것

스키마를 설정하는 것 : id(INT), name(TEXT) 등 속성을 설정하는 것

### 테이블(Table)

### 기본키 

### SQL(Structed Quesry Language)

## ORM(Object-Realational-Mapping)

Object: 객체(python) / Relational: RDBMS / Mapping : 연결 

***`객체지향 언어`를 `SQL`로 변환하는 프로그램***

python 코드는 DB와 통신불가. DB와 통신 가능한 언어는 SQL이다. 

따라서 ORM은 Python코드와 SQL 사이에서 번역해주는 프로그램이다. 

#### 파이썬에서 table표현법

1. 리스트 안의 딕셔너리(모든 호환 가능) [{}, {}, {}]
2. 객체 

Class Sutdent id = int, email = text

s1 = Student() s1.name= 'a'



## 사용모델 필드

CharField

TxtField(**options)

## migrate

이전하다. 

### [실습코드]

modle.py 

$ python managye.py makemigrations

$ python manage.py migrate

$ python manage.py shell_plus --print-sql

$ Student.objects.all()

[] Article.objects.create(title='aa', content='bb')

$ rm practice/migrations/0*

$ rm db.sqlite3

  created_at = models.DateTimeField()

  updated_at = models.DateTimeField()

auto_now_add : 생성

auto_now : update

[admin.py] from .models import Article

[admin.py] admin.site.register(Article) # admin에 model Article 등록

### Tagle 생성/ 수정 반영

1. model class 작성(수정) => 무조건 2번으로 
2. $ python manage.py makemigrations [app_name] (appname안쓰면 와랄랄라 생산됨)
3. $ python manage.py migrate [app_name]

### Data CRUD

#### ✨ Create

s1 = Student()

s1,name = 'a'

s1.age = 123

s1.majour = 'CS'

s1.save()

#### ✨Read (조회)

1. 단일 조회 Student.objects.all() # return qureyset
2. 전체 목록 Student.objects.get(id=1) # return object
3. 검색

####  ✨Update(수정)

 `s1 = Student.objects.get(pk=1)` **조회** 선행 필수 ! 

s1.is_married = True

`s1.save()` 저장이 중요 !

#### ✨ Delete(삭제)

 `s1 = Student.objects.get(pk=1)`

s1.delete()

[참고]

delete를 하고나서도 값이 남아있는 것 같은 이유

varchar/Text/모든 텍스트/ charfield/ TextField





[추가]

python <==> ruby 

깃허브, 깃랩, 카카오 rails 사용함

[추가2_실습]

urls => views => models => templates

Templates - dirs - BASE_DIR /'emplates'

`master url` 에 `import include`

`urlpatterns` = `path('articles/', include('practic.urls')),`

$ mkdir -p templastes/practice

$ touch urls.py 

touch article_datail.html article_list.html

from django.urls import path

from . import views

app_name = 'practice'

article = Article.objects.get(pk=article_pk)

articles = Article.objects.all()

{% load tz %} {{ article.created_at | localtime }}

{% url 'practice:article_detail' article.pk %}}



##  hws

id

title(<=200)

contexnt(TextField)

안녕하세요 / 반갑습니다 => 제목 / 내용

이글은 수정될거야 / 리얼루 =>  수정/ 완료

 ㅇㅇ / ㅇㅇ  => 삭제

django model fields

shell 실행 명령어 

## 정리

QuerySet api를 잘 해야함



### models.py

models.Model : 데이터베이스와 통신할 수 있는 능력이 생김

위를 상속받은 경우 

클래스는,  objects 라는 Manager를 두게됨

인스턴스는, 바로 실행 가능한 메서드 `.save()`가 존재 

`클래스`가 상징하는 것 `테이블`

`인스턴스`가 상징하는 것 `데이터 레코드 `

**클래스 == 테이블**

**인스턴스 == 데이터 레코드**

### CRUD

생성/ 조회/ 수정/ 삭제 

str method `__str__`

all() / get() : 아이디 1개만 / filter(): 여러개를 가져올 때/ delete() / exclude() 

### Database API

Airticle.objects.all()

- Manager(Object)
- QuerSet(중요함)

여러개의 데이터를 담는 것..

### Django Shell

`python manage.py shell/` -> 장고가 지원하는 것

`shell_plus` -> `django_extentions`가 지원하는 것

### AdminSite


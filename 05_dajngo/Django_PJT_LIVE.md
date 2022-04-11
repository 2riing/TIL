# Django 0304 PJT LIVE

## Namespace

URL namespace

Template namespace

namespace (이름공간)

객체를 구분할 수 있는 범위를 나타내는 말. 

하나의 이름공간에서는 하나의 이름이 단 하나의 객체만을 가르킨다. 

- 장고는 폴더를 임의로 만들어 줌으로써 이름공간을 설정 

### url app name

app_name = 'article'

### template namespace

app_name/templates/app_name 

## Static files

정적파일, 고정되어있는 파일 

ex) 사진 파일, css,  자바 스크립트 

서비스 중에도 추가되거나 변경되지 않고 고정되어있는 것

`staticfiles`라는 앱을 통해 관리중

### Static files 구성

`STATIC_URL`

```html
<img src= "{% static 'my_app/example.jpg' %}" alt="">
```



앱폴더 안에 static파일 안에 있다.

app/static/_________

### The static files app

- STATIC_URL

실제 파일이나 디렉토리가 아니며 URL로만 존재

- STATIC_ROOT

collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로 

**개발단계에서 동작하지 않음** 배포환경에서 사용하게 된다. 

아마존의 컴퓨터를 빌려서 배포하게 될 것

[참고] DEBUG = False : 배포단계에서 사용하는 것



### Django template tag

#### load

사용자 정의 탬플릿 태그 세트를 로드. 

로드하는 라이브러리 패키지에 등록된 모든 태그와 필터를 불러옴

#### static



### 정적 파일 사용하기 

** extends는 무조건 최상단에 있어야한다

static 폴더 안에 이미지 넣어주기 

SEETING = >

STATICFILES_DIRS =[

 

## 참고

깃 이그노어 목록

윈도우즈 vscode python django venv



1. 프로젝트 클론

2. 가상환경 생성

3. 가상환경활성화 후 패키지 목록 설치(`requirements.xtx`)

4. `.gitignore`작성

5. vscode 켜고 python interpreter 가상환경 잡고 vscode에서 터미널 켜고 시작

   


# 

## Favicon

Favicon(favorite icon) : 주소창, 탭 북마크바에 표시됨
link 태그임 <lint rel>
https://favicon.io (favicon 생성기)

HTML CSS 진행할 때는 경로 수정 필수 

href="/images/.."(X)
href="images/.."(O) ->상대경로

## Font

Font Awsome 

https://cdnjs.com/

https://fontawesome.com/

CDN링크 (공식문서에 없음)


## Icon


## CSS / SCSS 

** Complied CSS JS **

dist-css

** Souce Files **

SCSS (싸스) : CSS with Superpowers

Syntactically Awesome Style Sheets

CSS를 좀 더 쉽게 작성할 수 있게 함 

## 코드경량화(minify)

bootstrap.min.css

## Reboot.css / Reset.css / nomalize.css

초기화 해주는 것

각브라우저의 기본 스타일을 초기화


**가장 많이 실수했던 것**

modal : 관통에서 써야 됨

data-bs-toge="modal"

data-bs-target="#modal_id"

class 내에서 id = "modal_id

id를 일치시켜줘야함, 모달은 body에 써야함 

id와 data-bs-target"#id" 일치시킬 것

data-bs-toggle="moda;"

천천히 하는 것이 핵심이다.


## 시험 문제 정리 

### HTML(HyperText )
#### HTML 문서의 기본 구조(!-tab)
#### DOM
#### 시멘틱 태그
#### 주요 태그와 속성
(tale, form, input 안나옴)

### CSS
#### 단위(크기, 속성)
#### 선택자 및 우선순위
선택자 내용 다 정리해야함 
selector specificity(1,0,0)..

(1,0,0)
.id 

(0,1,0)
()
.class > .hi

(0,0,1)
table{

}

#### 박스모델 
전부 / 상하좌우(2개) / 상하(3개) / 시계방항(4개)

-> 무조건 나옴

#### 인라인, 블록 요소 특징

#### position
static (normal flow)
relative (normal flow)
absolute(out of flow)
fixed(out of flow)
Float(안나옴)
Flex
sticky

flex에 올인하시면 됩니다.
(align-content 제외)
(저스타파이 컨텐츠, 얼라인ㅇ ㅏ이템즈 얼라인 셀프 그로우 플로우 디렉션 플렉스 쇼텐드 메인축 컨테이너 이이템 개념)

### 반응형 웹
#### bootstaop
- grid system
- break poin




## 마크업

- 각 태그별 속성
- 
- 인라인, 블록
- 
- li-> liststyle

### 스타일링
### 레이아웃
display를 가지고 있는지 분석, Box model
-Position
네모위의 네모 :absolute
브라우저 기준 : fixed, sticky

-flex

-bootstrap Grid Sytem

### 스타일
- color

- size

- 각 태그별 속성

### 웹개발
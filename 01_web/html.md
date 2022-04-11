# HTML & CSS



## 서론




html & css 는 문서 작성 법이다.

프로그래밍적 요소 x ex) 마크다운



웹서핑을 하기 위해서는 브라우저가 필요한데

웹은 통일 되어있지 않았었다.





현재의 웹표준 : 브라우저간의 지원

WHATWG : 왓 위그 / 애플구글MS 등의 기업체 종심 

Web Hypertext Application Technology Working Group

W3C : 학계의 느낌



### 브라우저

크롬이 항상 높은 점수를 가지고 있다.

익스플로러는 312점.. 태생부터 .. 브라우저가 아니다.

엣지는 나쁘지 않음



Chrome Edge Whale Opera

구글스킨 ms스킨 네이버스킨 => 같은 orgin(chromium)을 가지고 있음



## 크롬 개발자 도구

F12버튼 

요쇼/element 탭이 가장 중요함



## HTML

Hyper Text Markup Language



Hyper Link를 통해 작성된 것 : Hyper Text





## HTML 기본 구조

```html
<html lang="ko">
<head>
    브라우저에 나타나지 않는 내용(문서 제목, 인코딩, 스타일, 외부 파일 로딩 등)
</head>    
<body>
    실제 화면 구성과 관련된 내용, 문서 본문 요소
</body>    
</html>
```

head 예시 title, mata (문서 레벨 메타데이터 요소), link. script, style



### haed : Open Graph Protocol

메타 데이터를 표현하는 새로운 규약

ex) 뉴스 기사를 카카오톡에서 어떻게 보여줄 것인가 



### DOM 트리 (Document Object tree)

HTML 문서를 브라우저가 이해하기 위한 구조 

뷰티풀숩 : 파서 

파싱 : 컴퓨터에서 [컴파일러](https://terms.naver.com/entry.nhn?docId=818396&ref=y) 또는 [번역기](https://terms.naver.com/entry.nhn?docId=840093&ref=y)가 [원시](https://terms.naver.com/entry.nhn?docId=851653&ref=y) 부호를 [기계어](https://terms.naver.com/entry.nhn?docId=828294&ref=y)로 번역하는 과정의 한 단계로, 각 문장의 [문법](https://terms.naver.com/entry.nhn?docId=824425&ref=y)적인 구성 또는 구문을 분석하는 과정. 

html은 인덴트(indent, 들여쓰기) 2space가 기본 





### 요소

- 요소는 태그&내용으로 구성
- 요소는 중첨이 될 수 있음

### 속성

```html
<a href="https://google.com"></a></a>
```

- 태그의 부가적인 정보 제공

key는 감싸지 않고 value는 쌍다옴표 



### HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성

id / class/ data-*/ style/ title/ tabindex



### 시맨틱 태그

- HTML5에서 의미론적인 요소를 담은 태그가 등장
- 검색 엔진 최적화(SEO)를 위해서 메타태그, 시맨틱 태그를 적극 활용 

div -> header/nav/section/aside/article/footer

시맨틱(semantic) 버전 : major miner bugfix (의미를 담은 버전)



### HTML 개발자 도구



인스펙터 : 마우스로 개발자도구 (컨+쉽+C)



## HTML 문서 구조화

### 텍스트 요소

```html
<a></a> 하이퍼링크 만들 때 
<b></b>
<strong></strong>
<i></i>
<em></em>
<br> 줄바꿈
<img> 이미지 표현
```

### 그룹 컨텐츠

```html
<p>
    문단
</p>
<pre></pre> 작성한 내용 그대로 표현
<blockquot> 인용문 </blockquot>
<hr> 수평선
<ol>
    순서 있는 리스트
</ol>
<ul>
    순서 없는 리스트
</ul>
```





### 인라인

줄바꿈이 안일어남 



간격은 <br>을 사용하지 않음



문서의 구조를 잡는데 브라우저의 기능이 도와주는건 필요 없음..

html 문법은 의미가 있을 때 사용하는 것



alt =" " 이건 꼭 써야함 



### form

양식

id/pw 등 로그인 정보를 한 번에 묶어서 보내는 기준 

### input

text/password/email/number/file

checkbox(중복 선택 가능) / radio button (한개만 선택 가능)

양식의 칸

잘 모르겠는 것 : id와 name의 차이 

for과 짝꿍 id

name = 키값

id = 라벨과 맞춰야하는 것 / 굉장히 여러곳에서 쓰이는 것



get / post는 대문자로 사용한다. 




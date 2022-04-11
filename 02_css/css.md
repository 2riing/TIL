# CSS

Cascading Style Sheets : 손탹헣 스타일을 지정하기 위한 언어

```css
h1{
    color: blue;
        font-size: 15px;
    
}
```

현실세계는 key value로 이루어져있다

선택자: h1

속성 : color , font=size

값 : blue, 15px



인라인과 박스에 대한 것은 중요함 



중괄호 안에 속성/값

## CSS의 정의방법 3가지

```css
1. <h1 style= ...> 인라인
2. <head>에 스타일 지정
3. <link rel="stylesheet" href...> 새로운 파일 만들기/ 외부참조
```



## Selector





ctl+enter : 다음줄로 넘어가기 

p.blue + tab

p#red.blue +tabl id: red class :blue





important랑 인라인 style 쓰지 마세요 



## css 기본 스타일

em/rem : 글자 스타일 (브라우저 기본 폰트에서 사용하는 것)

> viewport

vw, vh, vmin, ... 반응형 웹에서 사용하는 것 



### 색상단위

- 색상키워드
- RGB (rgb(0,0,0) rgba는 투명도까지 조정 가능)
- HSL (색상, 채도, 명도)

### 결합자

- 일반 형제 결합자

- 인접 형제 결합자



## Box model (중요함)

문서에는 박스만 존재함. 

위에서 아래로, 왼쪽에서 오른쪽으로 쌓임

- content : 실제 글이나 이미지
- padding : 테두리 안쪽의 내부 여백
- border : 테두리 영역
- margin : 외부여백
- content-padding-border-margin

margin 1px 2px 3px 4px (상우하좌 시계방향)





​      margin: 10px auto;

​	10px : 상하 

​	auto : 좌우 

​      /* 화면이 늘어나도 여전히 가운데! 반응형에 사용할 수 있을 듯 */





## CSS display

모든 요소는 박스 요소이고 좌측 상단에 배치 



display : block

display : inline





## CSS Position

absoulte vs relative



fixed : 어디에서든 그자리에 있어야하는 것 ex) 맨 위로 가기 



예전에는 이거 썼지만 요즘은 구시대의 유물이다. 최근에는 다른방식으로 정렬하고 있다.



## 개발자 도구 





## 마무리

html : 구조

CSS : 표시 
# 염수홍(A) README

 TMDB API를 활용해서 HOME과 영화 추천받기 탭을 구현하는 것



## 초기 설정/ 구조 잡기

가상환경에 `django 3.2.12` 버전을 설치

startproject `pjt04`를 통해서 프로젝트 생성

startapp `movies`로 무비 앱을 만들어주고 

`settings`의 앱 목록에 넣어준다. 

project의 `urls.py`에서 include를 통해 `moives`의 모든 url을 가져오고

app의 `urls.py` 에서도 url 경로 설정을 해준다. 

상위에 templates에는 base.html/ _nav.html / _footer.html을 생성

앱내의 tmeplates/movies에는 index.html/ recommendations.html을 생성해준다.



## API가져오기

pip install requests를 통해 모듈을 사용할 수 있게 한다. 

movies/views 의`recommendations`에서 movie 딕셔너리에 각 

제목, 포스터 이미지 경로, 설명, 평점, 개봉일을 받아온다.

그리고 variable routing을 통해 `recommadation.html` 에서 변수들을 활용한다. 



## 소감

api를 가져오는게 코드는 간단했지만, 생각해내기가 어려웠다.

시간이 부족했다,, 그래도 페어프로그래밍을 처음 해봤지만 재미있었다 🙌




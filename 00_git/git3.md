# git 3

https://gitcabinet.com/ 여기서 실습 가능



수업시간에 사용 할 명령어 add commit push clone pull

## git 초기 명령어



### git init

git init이란? -> 초기화

언제 git init을 하는지? -> git으로 관리가 되지 않고 있을 때, 

위치는? -> 최상단에서 

하위폴더에서는 사용하지 않기로 약속함 (가능하긴 함)



### git status(중요)

git이 수정, 생성, 삭제된 사항들을 표시해줌 

잘 잊어버릴 수 있는 것. add, commit push pull 보다 자주 사용하면서 상태 확인할 것



## Staging

ADD : 스테이징 에어리어에 올린다.



working directory 

 staging area (git이 추적을 시작함/ 변동을 기록하고 있는)



add를 왜쓰는지 모르겠음

add로 사진찍어놓고(스테이징 해놓고) commit으로 저장하는 건가?

무엇을 왜 추적하는지..?

add를 취소하는 것



취소가 가능함 



add staging -> 

commit만 삭제도 가능하고 add사실도 삭제할 수 있음

push 하고 나서도 add, commit , 파일지우기 전부 다 가능하다. 

git 공식문서에서 여러가지 볼 수 있음 

16진수로 되어있는 id값이 있음 과거로 여행 가능..

add . => 내 현재 위치에 있는 모든 것 (온점 == 현재 위치 )





add와 commit으로 버전관리하는 것

push : 업로드 하는 것 

repository : 외부 컴퓨터라고 생각하면 됨 





## origin

origin은 별명인

master가 작업한 것을 origin이라는 별명에 



```bash
git remote add origin + URL

git remote add gitlab + URL

git push gitlab master

git push github master
```





원격저장소 삭제 

```bash
git  remote remove origin
```





원격저장소 확인

```bash
gir remote -v
```



최초로 푸시할 때 

```bash
-u ??
set-upstream 의 약어 옵션 , 
작성 이유 : 미리 origin master만 하면 'git push'만 써도 가능
```



## clone & pull

```bash
git clone URL

git pull => 나에게 이미 git에 대한 정보가 있을 때,
```









## 계정설정

윈도우 자격 증명 관리자를 통해서 관리를 하는 것이 좋음.

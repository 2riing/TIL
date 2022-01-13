# 22년1월13일 (git)

## 💫Git에 대해서 배워보자💫
---

### 💥깃초기 설정(git 초기 설정)

```git
git init
```
`.git`이 생성. master 권한이 생김

```git 
rm -rf .git
```
**홈폴더에서 절대 하면 안됨**

```git
git config --global user.name "2riing"
git config --global user.email "2riing2@gmail.com"
```
깃에 이름과 이메일 입력
```git
git config --global user.name >2riing
git config --global user.email >2riing2@gmail.com
```
깃에 입력한 name&email 확인

초록불이 들어오고 있는 것은 U git이 관리하고 있는 것


### 💥add / 커밋하고 확인하기 
```git 
git add learn-git.md
```
`ADD` 명령어 : 스테이지에 올리기(스테이징)
```git 
git commit -m '1번 사진'
```
`커밋` 명령어 
```git 
git log
```
커밋된 것 `확인`
```git
git status
```
현재 파일들의 `상황을 확인 `

### 💥git 리파지토리 저장소 연결하기
```git
git remote add origin https://github.com/2riing/git-practice.git
```
로컬을 나의 `깃레파지토리(git-practice.git)에 연결`
```git
git remote -v
```
레파지토리에 `연결 된 것 확인`
```git
git push origin master
```
`깃푸시` 




### 기타 추가사항
#### 파일생성
```git 
touch learn-git.md
```
'learn-git'이라는 md파일 생성
```git
git --help
```
`도움`이 필요할 때 






           
           


윈도우키 - 자격 증명 관리자 - windows 자격 증명
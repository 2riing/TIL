# 22년1월13일 (git)

</br>
</br>
</br>

## 💫Git에 대해서 배워보자💫
---

### 💥깃초기 설정(git 초기 설정)

```git
git init
```
`.git`이 생성. master 권한이 생김

</br>

```git 
rm -rf .git
```
git 설정한 것 제거 **홈폴더에서 절대 하면 안됨**

</br>

```git
git config --global user.name "2riing"
git config --global user.email "2riing2@gmail.com"
```
</br>

깃에 이름과 이메일 입력
```git
git config --global user.name >2riing
git config --global user.email >2riing2@gmail.com
```
깃에 입력한 name&email 확인

초록불이 들어오고 있는 것은 U git이 관리하고 있는 것

</br>
</br>
</br>

### 💥add / 커밋하고 확인하기 
```git 
git add learn-git.md
```
`ADD` 명령어 : 스테이지에 올리기(스테이징)

</br>

```git 
git commit -m '1번 사진'
```
`커밋` 명령어

</br>

```git 
git log
```
커밋된 것 `확인`

</br>

```git
git status
```
현재 파일들의 `상황을 확인 `

</br>
</br>
</br>

### 💥git 리파지토리 저장소 연결하기
```git
git remote add origin https://github.com/2riing/git-practice.git
```
로컬을 나의 `깃레파지토리(git-practice.git)에 연결`

</br>

```git
git remote -v
```
레파지토리에 `연결 된 것 확인`

</br>

```git
git push origin master
```
`깃푸시` 

</br>
</br>
</br>

### 💥기타 추가사항
#### 파일생성
```git 
touch learn-git.md
```
'learn-git'이라는 md파일 생성
```git
git --help
```
`도움`이 필요할 때 

</br>

#### 윈도우키 - 자격 증명 관리자 - windows 자격 증명

</br>

#### 좋은 커밋 메시지
1. 영문 기준 50자
2. 제목 첫글자 대문자
3. 제목에 \. 금지 
4. 제목은 명령조로 (ex.Fix design error)
5. `무엇을`과 `왜`에 초점 


```git 
mv READMe.md README.md
```
`파일 이름 변경`하기

```git 
mv Jan13th.md /got
```
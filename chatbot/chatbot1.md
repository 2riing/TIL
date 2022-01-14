# 챗봇 만들기


## 텔레그램을 통한 챗봇 제작


### 파이썬 자료구조

- 리스트

```python 
tel = ['1234-1234', 'a', 1]
tel[2] = 1 
```


- 딕셔너리
```python
menu = {'한식' = ['김치찌개', '0000-0000]}
```


### 파이썬 반복문

</br>

- while
```python 
n = 0
while n<3:
    print(dust[n])
    n = n+1
```
n이 0일 때 dust[0]출력 , n이 1일 때 dust[1]출력 ... 2까지 

</br>

- for
```python
dust = [59, 24, 102]
for i in dust:
    print(i)
```
i가 1씩 늘어나면서 i=1 일 때 59, i=2일 때, 24.... 출력

+ 또다른 for문
```python
for i in range(5):
    print(insamal)
```
insamal 변수를 5회 반복

```python 
for i in range(1,46) 
```
1부터 45까지를 의미한다.

</br>
</br>

### 파이썬 내장함수 
1) print('hi') => hi
2) abs(-3) =>3
3) len('hi') =>2

</br>

파이썬의 내장함수는 셀 수 있는 정도이다.

외장함수는 import가 필수적이다.


### 파이썬 실행

git bash에서 파이썬 실행
```python
python lotto.py
python kospi.py
```
lotto.py 와 kospi.py를 실행 


### VSCODE를 통한 웹크롤링

`웹 크롤링` == 웹에서 기어다니면서 데이터를 가져오는 것
crawl = 기어가다. 

```bash
pip install beautifulsoup
```
파싱해주는 beautifulsoup를 받아옴 

돌도 씹어먹는 파싱 프로그램 

</br>

1) request.get(url) -> respose 202라고 실행됨
2) request.get(ulr).test ->드디어 내용을 받아옴
   
1) BeautifulSoup(문서)
2) BeautifulSoup.select(경로)
3) BeautifulSoup.select_one(경로)
   

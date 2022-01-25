# Python Data Structure (파이썬 데이터 구조)
## 순서가 있는 데이터 구조 
### 문자열
1. 조회/ 탐색
   
    1.1 .find(x)

        x의 첫 번째 위치를 반환
        x가 없으면 -1

    1.2 .index(x) 

        x의 첫 번째 위치를 반환
        x가 없으면 에러

    1.3 .startwith(x) .endwith(x)

        x로 시작하면 T
        아니면 F

2. 문자열 변경

    2.1 .replace(old, new[, count])

        새로운 글자로 바꿔서 반환
        count 지정하면 n만큼 시행 

    2.2 .strip([char]) .lstrip .rstrip

        공백을 지우거나 원하는 것을 지울 수 있음 

    2.3 .split([chars])

        글자 열을 나눌 수 있음 
        기본 값 : 공백
    
    2.4 .join
        접착제가 있음..

dir('string') : 메서드 확인 


### 리스트

많이 쓰는 것 : append pop count sord

1. 값 추가 및 삭제 => 원본 변경
 
    1.1 .append(x)


    1.2 .extend() - > 대박기능
        리스트에 리스트, 레인지, 튜플, 스트링 값을 붙일 수 있음

    1.3 .insert(i,x) * 이건 비추 정해진 위치에 값을 추가 가능

    1.5 .pop([i])

        정해진 위치 i 값을 삭제.
        i가 지정되지 않으면 마지막 항목 삭제 및 return 
    
    1.6 .clear()
        리스트의 모든 항목 삭제 


2. 정렬
    2.1 .index(x)

    2.2 .count(x)
        x의 개수를 센다.

    2.3 sort()

        값 자체를 변경해버림 

    2.4 .reverse() 
        반대로 뒤집기 
        reversed()는 저장 .reverse()는 1회성 


### 튜플
1. 탐색
    1.1 .count
    1.2 .index

많이 변경하고 싶은 경우
리스트로 변경
list((1,2,3))
        


## 순서가 없는 데이터 구조 
### 셋


### 딕셔너리 
1. 조회
    1.1 .get(key[, default])



### 얕은 복사 



### 깊은 복사 

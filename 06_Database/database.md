# Database



## DATABASE

체계화된 데이터의 모임

몇 개의 자료파일을 조직적으로 통합하여 

자료항목의 `중복`을 없애고 자료를 `구조화`한 집합체 

#### DB 용어정리 

- 스키마 : DB에서의 자료구조, 표현 방법 등 전반적인 명세를 기술

### RDB

### RDBMS

#### SQLite

파일 형태로 넣어서 사용하는 비교적 가벼운 데이터 베이스 

구글 안드로이드에 기본적으로 탑재된 데이터페이스

임베디드SW에서도 많이 활용됨

#### Sqlite Datat Type

1. Null
2. INTEGER
3. REAL
4. TEXT
5. BOLOB

## SQL
### 테이블 생성 및 삭제
### CRUD

CREATE

INSERT : 테이블에 단일행 삽입 

INSERT INTO 테이블이름(컬럼1, 컬럼2..) VALUES(값1, 값2...)

### WHERE
### AGGREGATE FUNCTIONS

집계 함수 : 값 집합에 대한 계산을 수행하고 단일 값을 반환

SELECT 구문에서만 사용됨 

ex) 테이블 전체 행 수를 구하는 COUNT(*)

COUNT, AVG, MAX, MIN, SUM

$ SELECT COUNT(컬럼) FROM 테이블 이름; (레코드의 개수 구하기)

### LIKE

패턴 일치를 기반으로 데이터를 조회하는 방법

` wildcards`를 제공 

`%`: 0개이상의 문자, 꼭 필요한건 아님

`_`(underscore) :임의의 단일 문자, 반드시 필요한 조건

### ORDER BY 

ASC - 오름차순(default)

DESC - 내림차순

$SELECT * FROM USERS ORDER BY age ASC LIMIT 10;

(오름차순 상위 10개 출력)

### GROUP BY

행 집합에서 `요약` 행 집합을 만듦

select문의 OPTIONAL절

**반드시 WHERE절 뒤에 작성해야함**

$ SELECT last_name COUNT(*) FROM users GROUP BY last_name;

(last_name 마다 사람이 몇명인지 세는 것)

### ALTER TABLE

table 이름변경 가능

테이블에 새로운 column추가 가능

sqlite 3.23 버전에서 column 이름 수정 가능











## 실습코드

$ sqlite webex.sqlite3

$ .database



## HWS

CREATE TABLE countries{}
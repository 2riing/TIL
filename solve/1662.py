# 압축되지 않은 문자열 S가 주어졌을 때, 
# 이 문자열중 어떤 부분 문자열은 K(Q)와 같이 압축 할 수 있다. 
# K는 한자리 정수이고, Q는 0자리 이상의 문자열이다. 
# 이 Q라는 문자열이 K번 반복된다는 뜻이다. 
# 압축된 문자열이 주어졌을 때, 
# 이 문자열을 다시 압축을 푸는 프로그램을 작성하시오.
# 첫째 줄에 압축된 문자열 S가 들어온다. S의 길이는 최대 50이다. 문자열은 (, ), 0-9사이의 숫자로만 들어온다.
# 33(562(71(9)))

#문자열 S받아오기

from this import d


S = '33(562(71(99999999)))'



# 문자열의 길이 l

l = len(S) 
n = 0

location = [0]*l

# 괄호가 있는 곳의 주소를  location 배열에 저장
# 문자열 길이 l만큼 반복
# 반복문(문자열 길이만큼 반복)/ 리스트 통해서 '('의 위치 저장 location[0]
# location 은 '('의 위치
# n : 괄호의 갯수

for i in range(l) :

    if S[i] == '(' :
        location[n] = i 
        n = n+1

print(S)
print("배열크기 : " + str(l))
print("괄호위치"+str(location))
print(n) 

# 괄호 개수 n이 3이면 0,1,2가 있다는 뜻. 그러면 n-1번째 괄호부터 시작 / 
# 해당 괄호 위치부터 시작 / 위치 임시저장 count
# count : 첫번째 괄호 위치 

count = location[n-1]

# K는 첫번째 괄호 왼쪽에 있는 숫자 1개 

K = S[count-1] 

# Q_count : count 부터 ')'가 나올 때 까지 숫자 길이 카운트
# n = 괄호가 있는 곳의 숫자 뒤 위치 
# if(S[1-count]==숫자라면)

i = count
# 첫괄호 오른쪽 위치부터 시작 
# 만약 숫자라면 Q_count ++ , 이 때 ')'이 등장하면  break
Qcount = 0

while i<l:
    i = i+1
    Qcount = Qcount + 1
    if (S[i] ==')'):
        break

# RealQcount= Qcount-1
# #한 번 더 센거 빼주기  RealQcount : 숫자인 문자열 갯수 이거 필요없음

# Q = int(S[i:RealQcount]) 
# print(Q) 

Q = S[count+1:count+Qcount]
print(Q)

W = K*Q 

# Q와 K가 변하면서 W에 여러번 저장 몇번? n번 

# W = K*Q
# num-1 W = K*Q ..... num-len(location) 이면 끝
# print(len(W))출력 

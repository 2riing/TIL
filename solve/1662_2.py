

S = '38(562(71(9879)))'

l = len(S) 
n = 0

location = [0]*l

for i in range(l) :

    if S[i] == '(' :
        location[n] = i 
        n = n+1


# 괄호 갯수 n개 저장 n번 해야함 순서 location[n-1] location[n-2] 인데 if n-z가 0이면 break




for y in range(n+1):
    count = location[n-y]
    K = S[count-1] 
    print(K)
    
        for z in range(l):
             Qcount = Qcount+1 
             if (S[count] ==')'):
             print(S[count+1:count+Qcount])
             break



    



    



#W = int(K)*int(Q) 

#print(len(W))

# Q와 K가 변하면서 W에 여러번 저장 몇번? n번 
# 변해야하는 것 count = location n-2 
# n-1,2,3.... 이 0이 나오면 그만둬야함

# W = K*Q
# num-1 W = K*Q ..... num-len(location) 이면 끝
# print(len(W))출력 

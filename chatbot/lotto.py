#random 모듈을 꺼낸다.
import random
# 1~45까지의 숫자통을 만든다.
numbers = range(1,46)
# 통에서 중에 6개를 랜덤으로 고른다
lucky = random.sample(numbers, 6)
print(lucky)
# 고른 숫자를 출력 


num = range(2,12)
for i in range(10):
    if(num[i]%2==0):
        print('woo')
    else:
        print('ha')

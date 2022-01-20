# 숫자를 받아서- input
# 세제곱 결과를 반환 - output
# 호출 : cube(2), cube(10) ...
def cube(number):
    return number ** 3
    # 세제곱 해주는 함수 
print(cube(2))


# values = list()

# values[
# 	{'name' = ['염수홍', '조용준', '이우현']
# 	 'age' = '29'	
# ]


# values[0]['name'][0]

def add(a, **args):
	return a, args

print(add(2, b=2))
# print(add(2, a=100, b=2)) 는 에러 

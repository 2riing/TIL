# values = list()

# values[
# 	{'name' = ['염수홍', '조용준', '이우현']
# 	 'age' = '29'	
# ]


# values[0]['name'][0]

def add(a, **args):
	return a, args

print(add(2, a=100, b=2))
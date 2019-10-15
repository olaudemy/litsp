def verify_palindrom(data):
	data1 = data.upper().replace(' ','')
	data2 = data1[::-1]
	if data2 == data1:
		print("YES")
	else:
		print("NO")

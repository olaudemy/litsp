def verify_palindrom(data):
	data1 = data.upper().replace(' ','')
	data2 = data1[::-1]
	if data2 == data1:
		return("YES")
	else:
		return("NO")

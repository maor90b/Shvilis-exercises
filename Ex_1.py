def find_largest(arr,k):
	"""This func return k highest numbers in arr"""
	if k > len(arr):
		k = len(arr)
	higest_numbers = []
	for i in range(k):
		higest_numbers.append(arr.pop(arr.index(max(arr))))
	return higest_numbers


# option 2

def find_largest2(arr,k):
	"""This func return k highest numbers"""
	if k > len(arr) or k < 1:
		k = 1
	arr.sort(reverse=True)
	highest = []
	for i in range(k):
		highest.append(arr[i])
	return highest

print(find_largest2([8,4,5,1,70,50,80,30,50], 2))


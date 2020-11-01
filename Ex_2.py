"""7 Boom"""

def div_7(arr):
	"""This func return num from arr that divide with 7 without residue"""
	for i in arr:
		if i % 7 == 0:
			print(i,'Boom!')

# div_7([7,5,1,21,254,56,42,2100])


def div_7_2(arr):
	if type(arr)==dict:
		arr=arr.values()
	arr2 = list(filter(lambda x: x%7==0, arr))
	for i in arr2:
		print(i, 'Boom!')

div_7_2({1: 7,2: 5,3: 1,4:21})



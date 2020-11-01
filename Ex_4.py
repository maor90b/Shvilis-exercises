# Return reversed num
def reversed_num(num):
	"""This func return reversed num"""
	new_num = 0
	while num // 10 > 0:
		new_num += num % 10
		new_num *= 10
		num //= 10
		if num // 10 == 0:
			new_num += num % 10
	print(new_num)



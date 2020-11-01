# sent = "Hello"
#
# def let(a):
# 	linked = lambda x: a+x
# 	return linked
# word=let('maor')
# print(word(' bartov'))
#
#
# def split_word(word):
# 	l1=[char for char in word]
# 	return l1
#
# def repeat_let(s):
# 	l1=set(split_word(s))
# 	return list(l1)
#
# print(repeat_let('mmmmma'))

strlist = ['bob maor', 'sami shvili', 'shvulu luku']

# strlist.sort(key=lambda x: x.split(" ")[1])

def map_reduce(sentence):
	"""mapr reduce characters in string"""
	sentence = sentence.replace(' ','')
	chars = [char for char in sentence]
	chars_2 = set(chars)
	chars_3=[]
	for i in chars_2:
		count = chars.count(i)
		chars_3.append((i,count))
	return chars_3

print(map_reduce('mmmbbb ccc ssss'))








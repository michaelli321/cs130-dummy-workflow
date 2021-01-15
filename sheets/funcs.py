def func_1(num: int) -> int:
	if num < 0:
		return -1
	elif num == 0:
		return 1
	else:
		return func_1(num-1)

def func_2(letter: str) -> int:
	return ord(letter)

def func_3(str1: str, str2: str) -> str:
	return str1 + str2
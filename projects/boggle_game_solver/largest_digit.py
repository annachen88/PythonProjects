"""
File: largest_digit.py
Name: Anna
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: integer
	:return: string
	"""
	n = str(n)
	if len(n) == 0:
		return n
	elif len(n) == 1:
		return n
	else:
		if n[0].isdigit():
			if not n[-1].isdigit() or n[0] >= n[-1]:
				return find_largest_digit(n[0:len(n) - 1])
		return find_largest_digit(n[1:len(n)])


if __name__ == '__main__':
	main()

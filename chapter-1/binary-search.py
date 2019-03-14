def binary_search(s_list, item):
	low_pos = 0
	high_pos = len(s_list) - 1

	while low_pos <= high_pos:
		mid_pos = int((low_pos + high_pos) / 2)
		guess = s_list[mid_pos]

		if guess == item:
			return mid_pos
		if guess < item:
			low_pos = mid_pos + 1
		else:
			high_pos = mid_pos - 1

	return None


s_list = [1,2,3,4,5,6,7,8]
item = binary_search(s_list, 7)

print(f'position: {item}')

def binary_search(sequence, item):
	begin_index = 0 
	end_index = len(sequence) - 1
	while begin_index <= end_index:
		print("loop working")
		mid_point = begin_index + (end_index - begin_index) // 2
		mid_point_value = sequence[mid_point]
		if mid_point_value == item:
			print("loop ending, midpoint equals item")
			return mid_point
		elif item < mid_point_value:
			print("item is smaller than midpoint")
			end_index = mid_point - 1
		else:
			print("item is larger than midpoint")
			begin_index = mid_point + 1 
	print("loop fails")
	return None


sequence_a = [1,2,3,4,5,6,7,8,9,10,11,12,23,45,67,89]
item_a = 12

print(binary_search(sequence_a, item_a))
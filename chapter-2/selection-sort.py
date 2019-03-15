def findSmallestIndex(arr):
	smallest = arr[0]
	smallest_index = 0;
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index
	
#print(findSmallestIndex([5,0,8,3,6,1]))

def selectionSort(arr):
	sorted_array = []
	for i in range(len(arr)):
		smallest_index = findSmallestIndex(arr)
		sorted_array.append(arr.pop(smallest_index))
	return sorted_array

print(selectionSort([5,0,8,3,6,1]))



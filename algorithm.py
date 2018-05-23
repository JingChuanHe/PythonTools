def sort(arr):
	for  i in range (0,len(arr)):
		print(arr,i)
		for j in range(i+1,len(arr)):
			if arr[i] < arr[j]:
				m = arr[i]
				arr[i] = arr[j]
				arr[j] = m


if __name__ == '__main__':
	arr = [2,4,6,3,7,4,8]
	print('Begin sort',arr)
	sort(arr)
	print('After sort',arr)
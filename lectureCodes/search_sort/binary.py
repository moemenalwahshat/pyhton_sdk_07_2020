def binary_search(l,item):
	left = 0
	right = len(l)-1
	found = False
	while( left<=right and not found):
		mid = ( left + right )//2
		if l[mid] == item :
			found = True
		else:
			if item <l[mid]:
				right = mid - 1
			else:
				left = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,12,2,8], 2))
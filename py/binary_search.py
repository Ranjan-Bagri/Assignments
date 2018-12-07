from math import floor

def bin_search(arr,t):
	l=0
	n=len(arr)
	r=n
	
	while l<r:
		m=floor((l+r)/2)
		if arr[m]<t:
			l=m+1
		else:
			r=m
	return l

print((bin_search([-56, -3, 4, 9, 12, 22, 78],12)))

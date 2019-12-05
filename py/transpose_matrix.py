a=[[1,2],
	 [3,4]]
print(a)

def tr(a):
	rows=len(a)
	cols=len(a[0])
	k=[[0]*rows for i in range(cols)]
	for j in range(rows):
		for i in range(cols):
			k[i][j]=a[j][i]
	return k

print(tr(a))
		
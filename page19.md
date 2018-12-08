<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the transpose of a matrix


### Desciption:

Transpose of a matrix is an operator that switches the row and column indices of the original matrix and produces another matrix denoted as \\(A^T\\) by flipping the original matrix over its diagonal.

Let \\(A\\) be an \\(m\times n\\) order matrix, then dimension of \\(A^T\\) will be \\(n\times m\\).

Therefore the \\(i^{th}\\) row, \\(j^{th}\\) column element of \\(A^T\\) is the \\(j^{th}\\) row, \\(i^{th}\\) column element of \\(A\\).

for example,
\\[{\begin{bmatrix}1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}}^{\operatorname {T}}=\begin{bmatrix}1 & 3 & 5 \\ 2 & 4 & 6 \end{bmatrix}\\]

### Implementation:

<kbd>Input</kbd>

```python
a=[[1,2],
	 [3,4],
	 [5,6]]
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
		
```

<kbd>Output</kbd>

```python
[[1, 2], [3, 4], [5, 6]]
[[1, 3, 5], [2, 4, 6]]
```

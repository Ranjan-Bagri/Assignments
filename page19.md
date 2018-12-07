<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## transpose of a matrix


### Desciption:


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

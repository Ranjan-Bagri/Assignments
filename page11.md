<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## Binary search


### Desciption:
Binary search is a searching algorithm that finds the position of a target value within a sorted list.

Let an \\(A\\) be a list of \\(n\\) elements with values \\(a_0,a_1,a_2,\cdots,a_{n-1}\\) sorted such that \\(a_0\leq a_1\leq a_2\leq \cdots \leq a_{n-1}\\) and the target value is \\(T\\).

Binary search begins by comparing the middle element of the list with the target value. If the target value matches the middle element, its position in the list is returned. If the target value is less than the middle element, the search continues in the lower half of the list untill the posotion of \\(T\\) is returned.

### Implementation:

<kbd>Input</kbd>

```python
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
```

<kbd>Output</kbd>

```python
4
```

[Try it online!](https://tio.run/##TY7LCoMwFETXuV9xlwlGWrVvzJeIFNtGEshDrimlX2@jqy4GhuFwmOmbTAzNsowUPfohGbR@ipRwdDESwEuP@LDhPuuBnoYPRDKJGzCn9sCCcjqsmwBGKgAD9jHWaXQtZYZ5tVk4dwWJXZ0pZkfMfOf7Nq1E9viiykW7WW8DKZ9lOr0poAOYyIbE@d@FrjyeJJaNxIPEq8SqlljnnC@9rGohxLL8AA "Python 3 – Try It Online")

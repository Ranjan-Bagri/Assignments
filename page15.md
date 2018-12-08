<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To estimate the value of pi(\\(\pi\\)) (Monte-carlo method)


### Desciption:


### Implementation:

<kbd>Input</kbd>

```python
from random import *

def pi(n):
	square=0
	circle=0
	while square<n:
		x=random()
		y=random()
		if ((x**2+y**2)<=1):
			circle+=1
		square+=1
	return (circle/square)*4

print(pi(5000000))
```

<kbd>Output</kbd>

```python
3.1422552
```
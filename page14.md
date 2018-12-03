<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## Program to determine approximate area of a circle


### Desciption:


### Implementation:

<kbd>Input</kbd>

```python
from random import *
r=float(input('radius='))

def area(n):
	square=0
	circle=0
	while square<n:
		x=random()*r
		y=random()*r
		square_area=((2*r)**2)
		if ((x**2+y**2)<=(r**2)):
			circle+=1
		square+=1
	return (circle/square)*square_area

print(area(500000))
```

<kbd>Output</kbd>

```python
radius=6
113.062752
```

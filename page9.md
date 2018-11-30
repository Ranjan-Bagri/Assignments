<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To estimate the value of pi


### Desciption:


### Implementation:

<kbd>Input</kbd>

```python
from math import sqrt,cos,radians

def estimate_pi(length,n):
	radius = float((length)/(sqrt(2-2*(cos(radians(360/n))))))
	diameter = 2*radius
	c = (length*n)
	return float(c/diameter)
	
print((estimate_pi(1,500000)))
```

<kbd>Output</kbd>

```python
3.141592770102689
```

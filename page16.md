<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## Program to determine approximate volume of a sphere


### Desciption:


### Implementation:

<kbd>Input</kbd>

```python
from random import *
r=float(input('radius='))

def volume(n):
	cube=0
	sphere=0
	while cube<n:
		x=random()*r
		y=random()*r
		z=random()*r
		cube_volume=((2*r)**3)
		if ((x**2+y**2+z**2)<=(r**2)):
			sphere+=1
		cube+=1
	return (sphere/cube)*cube_volume

print(volume(500000))
```

<kbd>Output</kbd>

```python
radius=6
906.2426879999999
```

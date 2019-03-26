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


[Download]

or

[Try it online!](https://tio.run/##VU9LEoIwDF3TU3RnUhaijC4cehYHpQydgbYTWhUuj62wkCyS9/J5SdzkO2vKZWnJDpxq08SgB2fJc8FItr2tPWjjgocD1Y0OozwgMtaolr9sHwYFBm8se4aHkgXLRtcp@qF3p3vFU74ysSH7yFUeUFCk057Oe5rG7qu@BDgLQiFKjAXdcoCPEOd8Sm6ODisJlGK6I9suyOVpk/khUj6Q4bAWjymP4m8JY4608bC9dCmSIS7L9Qs "Python 3 – Try It Online")

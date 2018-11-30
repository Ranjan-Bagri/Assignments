<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the surface area and volume of a sphere


### Desciption:

If the radius of a sphere is denoted by \\(r\\) then its surface area is
\\[A=4\pi r^2\\]
And volume is
\\[V=\frac{4}{3}\pi r^3\\]

### Implementation:

<kbd>Input</kbd>

```python
from math import pi
radius=float(input('Enter a number: '))

area=4*pi*(radius**2)
print("Surface area of the sphere is %3f"%area)

volume=(4/3)*pi*(radius**3)
print("Volume of the sphere is %3f"%volume)
```

<kbd>Output</kbd>

```python
Enter a number: 6
Surface area of the sphere is 452.389342
Volume of the sphere is 904.778684
```

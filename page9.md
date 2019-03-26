<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To estimate the value of pi


### Desciption:

Let a regular polygon of side \\(n\\) be circumscribed by a circle of redius \\(r\\).

[![estimation_of_pi](https://gribja.github.io/Assignments/img/inscribed_hexagon.jpg)](https://gribja.github.io/Assignments/img/inscribed_hexagon.jpg)

for \\(\Delta EOF\\)    \\(\angle EOF=\theta\\)

And \\(\overline{OE}=\overline{OF}=r\\)

Since the polygon is regular, the angle made by each side
\\[\theta =\frac{360^{\circ}}{n}\\]

Let \\(\overline{OE}=a\\), \\(\overline{OF}=b\\), \\(\overline{EF}=c\\)

Therefore using the law of cosine we get
\\[c^2=a^2+b^2-2ab\cos{\theta}\\]
\\[c^2=2r^2-2r^2\cos{\frac{360^{\circ}}{n}}\\]
\\[c=r\sqrt{2\left(1-\frac{360^{\circ}}{n}\right)}\\]

circumference = \\(nc\\)

diameter = \\(2r\\)

\\[\pi = \frac{nc}{2r}\\]


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


[Download]

or

[Try it online!](https://tio.run/##TY7BDoIwEETP9Ct6LKQGhOjBxG8xDRRpQrdluxz8@rpoTZzb7sy83fiiJcCQ84zBS29okc7HgCTThqTHkDSayRlIQkx2ljaR45R9RKdWC09aNNQ3UR2hPcm7nNdgSBWvbtWBUf2pbxSzVGGp4dq1UH8kKl55Sxa53TdfkKhGngqlAQ6hpR2h4Mf212FHRHTAJ/9fO@tLd4j5Ob8B "Python 3 – Try It Online")

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the approximate value of definite integral using simpson rule


### Desciption:

Let \\(f(x)\\) be a function integrable from \\(x=a\\) to \\(x=b\\)
\\[I(a,b) = \int^b_a f(x)dx\\]

[![simpson rule](https://gribja.github.io/Assignments/img/simpson.jpg)](https://gribja.github.io/Assignments/img/simpsons.jpeg)

Geometrically, \\(f(x)\\) represents a curve

We can devide the area under the curve into \\(n\\) slices, each side having the width \\(h=\frac{b-a}{n}\\)

If the curve \\(f(x)\\) fits a quadratic polynomial \\(Ax^2+Bx+C\\) and \\(-h,0,+h\\) are three points, then
\\[f(-h) = Ah^2-Bh+C\\]
\\[f(0) = C\\]
\\[f(h) = Ah^2+Bh+C\\]

\\[\Rightarrow A=\frac{1}{h^2}[\frac{1}{2}f(-h)+f(0)+\frac{1}{2}f(h)],\\]
\\[B=\frac{1}{2h}[f(-h)-f(h)],\\]
\\[C=f(0)\\]

the areaunder the curve from \\(-h\\) to \\(h\\) is approximated by the area under the quadratic, so
\\[\int^h_{-h} (Ax^2+Bx+C)dx \\]
\\[= \frac{2}{3}Ah^3+2Ch\\]
\\[= \frac{1}{3}h[f(-h)+4f(0)+f(h)]\\]

Since the rule approximate the area under two adjacent slices,

\\[\therefore I(a,b) = \frac{1}{3}h \left[f(a)+f(b)+4\sum_{k=1,k (odd)}^{n-1} f(a+kh)+2\sum_{k=2,k (even)}^{n-2} f(a+kh)\right]\\]

### Implementation:

<kbd>Input</kbd>

```python
def f(x):
	return x**4-5*x**3+7

def simp(func,a,b):
	n = 1000000
	h = (b-a)/n
	c=d=0
	for i in range(1,n,2):
		c += func(a+i*h)
	for j in range(2,n,2):
		d += func(a+i*h)
	return (1/3)*h*(func(a)+func(b)+4*c+2*d)


print(simp(f,5,10))
```

<kbd>Output</kbd>

```python
13472.470833366839
```

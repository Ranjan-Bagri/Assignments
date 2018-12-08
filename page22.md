<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the approximate value of definite integral using trapezoidal rule


### Desciption:

Let \\(f(x)\\) be a function integrable from \\(x=a\\)to \\(x=b\\)
\\[I(a,b) = \int^b_a f(x)dx\\]

Geometrically, \\(f(x)\\) represents the curve in \\([a,b]\\)

We can devide the area under the curve into \\(n\\) slices of trapezoids, each side having the width \\(h=\frac{b-a}{n}\\)

The area of a trapezoid of base \\(h\\) and sides \\(c,d\\) is \\(A=(c+d)\frac{h}{2}\\)

If the RHS of \\(k_{th}\\) slice occurs at \\((a+kh)\\) and the LHS of it at \\(a+(k-1)h\\), the area of that trapezoid will be
\\[A_k=\frac{1}{2}h[f(a+(k-1)h)+f(a+kh)]\\]
\\[\therefore I(a,b) \approx \sum_{k=1}^n A_k = \frac{1}{2}h \sum_{k=1}^{n} [f(a+(k-1)h)+f(a+kh)] \\]
\\[I(a,b)=h[\frac{1}{2}f(a)+\frac{1}{2}f(b) + \sum_{k=1}^{n-1} f(a+kh)]\\]

### Implementation:

<kbd>Input</kbd>

```python
def f(x):
	return x**4-2*x+1

def trap(func,a,b):
	n = 1000000
	h = (b-a)/n
	s = (1/2)*(func(a)+func(b))

	for i in range(1,n):
		s += func(a+i*h)
	return h*s


print(trap(f,0,2))
```

<kbd>Output</kbd>

```python
4.400000000010726
```

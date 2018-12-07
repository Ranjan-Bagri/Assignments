<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## trapezoidal rule


### Desciption:


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

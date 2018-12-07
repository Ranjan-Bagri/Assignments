<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## simpson rule


### Desciption:


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

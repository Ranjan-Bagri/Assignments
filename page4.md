  <script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find \\(n\\) terms of Fibonacci sequence

## Description:

Fibonacci sequence is an integer sequence characterized by the fact that every number after first two is the sum of two preceding ones.
If the \\(n^{th}\\) terms of the sequence is denoted by \\(F_n\\), the sequence can be represented by a recurrence relation
\\[F_n=F_{n-1}+F_{n-2}\\]

### Implementation:

<kbd>Input</kbd>

```python
def fibonacci(n):
	a=0
	b=1
	for i in range(n):
		if i<=0:
			print(a)
		elif i==1:
			print(b)
		else:
			c=a+b
			a=b
			b=c
			print(c)
		
fibonacci(10)
```

<kbd>Output</kbd>

```python
0
1
1
2
3
5
8
13
21
34
```

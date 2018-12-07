<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## prime number


### Desciption:


### Implementation:

<kbd>Input</kbd>

```python
def prime(n):
	k=0
	if n>1:
		for i in range(2,n):
			if (n%i==0):
				k+=1
		if (k<=0):
			return '%s is a Prime number'%n
		else:
			return '%s is not a Prime number'%n
	else:
		return '%s is not a Prime number'%n

a=int(input('Enter a Natural number: '))
print(prime(a))
```

<kbd>Output</kbd>

```python
Enter a Natural number: 7
7 is a Prime number
```

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To check if a given number is prime or not


### Desciption:

Let \\(n\\) be a natural number.

Now, \\(n\\) is a prime number if it is greater than one and if none of the numbers \\(2,3,\cdots,n-1\\) devides \\(n\\) evenly.

Since every natural number has both \\(1\\) and itself as a divisor, \\(n\\) won't be prime if it has any other divisor than \\(1\\) and \\(n\\) itself.

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


[Download](py/prime_number.py)

or

[Try it online!](https://tio.run/##jdCxDoIwEAbguX2KW0jb6AA6mBDq5mp8hRoPvQAHKWXw6WsR2Rgc/z/f5XI3vMOr52OMD6xh8NShZlNK0dhcCqqBz0VKou49EBCDd/xEfdh/kZiF5oyszZcsmp0t5NI31dp6DJNnUNkINIKD27wHeOru6FXGiWA74gblPmzxVf@DpbPEQRMPU9DqwgF9UleXJl37cyUoY2S6PsHlB86YGE8f "Python 3 – Try It Online")

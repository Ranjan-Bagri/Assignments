<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To calculate cosine value of an angle using cosine series


### Desciption:


### Implementation:

<kbd>Input</kbd>

```python
import math

def cos(x,n):
	cosine=0
	y=x*(math.pi/180)
	for i in range(n):
		sign=(-1)**i
		cosine+=(((y**(2*i))/(math.factorial(2*i)))*sign)
	return cosine

x=int(input('Enter the value in degree: '))
n=int(input('Enter the number of terms: '))

print(round(cos(x,n),3))
```

<kbd>Output</kbd>

```python
Enter the value in degree: 60
Enter the number of terms: 10
0.5
```

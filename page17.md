<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To calculate sine value of an angle using sine series


### Desciption:

Sine series is a convergent infinte series produced by applying Maclaurin's series on \\(sin\\ function.

\\[\therefore \sin (x) = x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots\\]
\\[\forall x\in R\\]
\\[= \sum_{i=0}^{\infty} \frac{(-1)^i}{(2i+1)!} x^{2i+1}\\]

For first \\(n\\) terms of expansions

\\[ \sin (x) = \sum_{i=0}^{n} \frac{(-1)^i}{(2i+1)!} x^{2i+1}\\]

If \\(x\\) is expressed in degrees then the series would contain a factor of \\(\frac{\pi}{180}\\)

\\[\therefore \sin (x_{deg}) = \sum_{i=0}^{n} \frac{(-1)^i}{(2i+1)!} \left(\frac{\pi x}{180}\right)^{2i+1}\\]

### Implementation:

<kbd>Input</kbd>

```python
import math

def sin(x,n):
	sine=0
	y=x*(math.pi/180)
	for i in range(n):
		sign=(-1)**i
		sine+=(((y**(2*i+1))/(math.factorial(2*i+1)))*sign)
	return sine

x=int(input('Enter the value in degree: '))
n=int(input('Enter the number of terms: '))

print(round(sin(x,n),3))
```

<kbd>Output</kbd>

```python
Enter the value in degree: 30
Enter the number of terms: 10
0.5
```


[Download](py/sin.py)

or

[Try it online!](https://tio.run/##bY@xbsMwDERn8yu0hVLSxo6XIoDGfoha0zaBmBIUqbC/3pUSZMt2PDwej2FLs5d@33kJPia1uDQDDDSqOwuuJ9FXaIok20Kz2dVgJT4Dn7uvVkMz@qhYsajoZCJ84IWfxOJHp43hxyh0tIi4GYMXw8dO6/MzZ3S/yUd2t5evTV0uwZFSjlJbEMBqWRKyhJzw8C2JokozqT93y1SPDzRFoqs6aA3ynpW8/BTpR1Wc5f5kIcQKR59lwNfDp17rfe9b6Np/ "Python 3 – Try It Online")

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To calculate cosine value of an angle using cosine series


### Desciption:

Cosine series is a convergent infinte series produced by applying Maclaurin's series on \\(cos\\) function.

\\[\therefore \cos (x) = x-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots\\]
\\[\forall x\in R\\]
\\[= \sum_{i=0}^{\infty} \frac{(-1)^i}{(2i)!} x^{2i}\\]

For first \\(n\\) terms of expansions

\\[ \cos (x) = \sum_{i=0}^{n} \frac{(-1)^i}{(2i)!} x^{2i}\\]

If \\(x\\) is expressed in degrees then the series would contain a factor of \\(\frac{\pi}{180}\\)

\\[\therefore \cos (x_{deg}) = \sum_{i=0}^{n} \frac{(-1)^i}{(2i)!} \left(\frac{\pi x}{180}\right)^{2i}\\]

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


[Download](py/cos.py)

or

[Try it online!](https://tio.run/##bY/BboMwEETP@Cv2lrWbNtBIURXJx36IGxZYKawtY1fw9dTU6q232dGbWU3Y0uTluu88Bx8TzC5NSvU0wMMvuJ5F31VTJAvZVjWbXQ0ezFvgS/fRatUMPgIDC0QnI@FvoFl4FIuvnTaGy1kLXiwibsbgu2GtL7VncI/kI7tndbU5oqU2UspRoCaVWi1LQpaQE54@JVGENBF8u2em43lPYyS6w0lrJf@zkuevIv0AxZmXyqoQDzj6LD3@TT5ftd73W6u69gc "Python 3 – Try It Online")

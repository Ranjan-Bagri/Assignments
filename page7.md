<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the area and circumference of a circle


### Desciption:

If the radius of a circle is denoted by \\(r\\) then its circumference is
\\[S=2\pi r\\]
And area is
\\[A=\pi r^2\\]

### Implementation:

<kbd>Input</kbd>

```python
from math import pi
radius=float(input('Enter a number: '))

area=pi*(radius**2)
print("Area of the circle is %3f"%area)

circumference=2*pi*radius
print("Circumference of the circle is %3f"%circumference)
```

<kbd>Output</kbd>

```python
Enter a number: 6
Area of the circle is 113.097336
Circumference of the circle is 37.699112
```


[Download]

or

[Try it online!](https://tio.run/##dcw9CsMwDIbh3acQgRDbYwIdChlKyUHcVCaC@AdFHnp6NyEU2qGrPr1PfsmS4lCr5xQgOFmAQk4skEmxe1LZRr8mJ5piLqK7KQoyOIglPJCv0BmjlGN0Yyarz8La3qjMFEU3t32C5EEWhJl4XhFog3bwTXtUe3xcS/DIGGcce7s7J/Mh7t8Pf6wfxNR6eQM "Python 3 – Try It Online")

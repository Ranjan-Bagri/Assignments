<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>


## To find the area of any triangle from its given sides


### Desciption:

If the lengths of three sides of any triangle is denoted by \\(a\\),\\(b\\) and \\(c\\) respectively, then the half-perimeter of the triangle will be
\\[S=\frac{(a+b+c)}{2}\\]
Therefore, the area will be
\\[A=\sqrt{s(s-a)(s-b)(s-c)}\\]


### Implementation:

<kbd>Input</kbd>

```python
a=float(input('Enter the length of side a: '))
b=float(input('Enter the length of side b: '))
c=float(input('Enter the length of side c: '))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is %3f"%area)
```

<kbd>Output</kbd>

```python
Enter the length of side a: 3
Enter the length of side b: 4
Enter the length of side c: 5
Area of triangle is 6.000000
```


[Download]

or

[Try it online!](https://tio.run/##jcxNDoMgEIbhPaeYmBgZTH9SddOERRc9yEBBSQwamC56elrrBdy8q@f71g9PS@xKIe3nhViGuL5ZNs/ILgFPDmYXR55g8ZDDywHdoUEU5iA3O7cHud151pJa01q83AQlR1pmJfOJcKv51yIqdT0PYk0hsqweP7bdcAoUx9lByFB3vqq3PZbSiV4MXw "Python 3 – Try It Online")
